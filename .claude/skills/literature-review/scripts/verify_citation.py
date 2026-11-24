#!/usr/bin/env python3
"""Check one reference against Crossref and arXiv. Prints one JSON object.

Only the title, first author and year are sent to the public APIs, never any
manuscript text.

Usage:
    python3 verify_citation.py --title "Attention is all you need" --author Vaswani --year 2017
    python3 verify_citation.py --title "..." --author Smith --year 2021 --doi 10.1000/xyz

Verdict values: match, mismatch, not_found.
Matching rules: title ratio >= 0.90 after normalising, first author surname
equal, year within one year (preprint versus published).
"""
import argparse
import difflib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

CROSSREF = "https://api.crossref.org/works"
ARXIV = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}


def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return " ".join(t.split())


def title_ratio(a, b):
    return difflib.SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


def surname(name):
    name = (name or "").strip()
    if "," in name:
        return name.split(",")[0].strip().lower()
    parts = name.split()
    return parts[-1].lower() if parts else ""


def judge(want, found):
    """Compare wanted fields with one found record. Returns (verdict, notes)."""
    notes = []
    ratio = title_ratio(want["title"], found.get("title", ""))
    if ratio < 0.90:
        return "mismatch", ["title similarity %.2f is below 0.90" % ratio]
    ok = True
    if want.get("author"):
        if surname(want["author"]) != surname(found.get("first_author", "")):
            ok = False
            notes.append("first author differs: wanted %s, found %s"
                         % (want["author"], found.get("first_author", "?")))
    if want.get("year") and found.get("year"):
        try:
            if abs(int(want["year"]) - int(found["year"])) > 1:
                ok = False
                notes.append("year differs: wanted %s, found %s" % (want["year"], found["year"]))
        except ValueError:
            pass
    return ("match" if ok else "mismatch"), notes


def get(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "research-agent/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < retries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            raise
        except urllib.error.URLError:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            raise


def crossref_candidates(title, author, doi, mailto):
    if doi:
        url = CROSSREF + "/" + urllib.parse.quote(doi)
        if mailto:
            url += "?mailto=" + urllib.parse.quote(mailto)
        items = [json.loads(get(url).decode())["message"]]
    else:
        q = {"query.bibliographic": title, "rows": 3}
        if author:
            q["query.author"] = author
        if mailto:
            q["mailto"] = mailto
        items = json.loads(get(CROSSREF + "?" + urllib.parse.urlencode(q)).decode())["message"]["items"]
    out = []
    for it in items:
        authors = it.get("author") or []
        issued = (it.get("issued") or {}).get("date-parts") or [[None]]
        out.append({
            "source": "crossref",
            "title": (it.get("title") or [""])[0],
            "first_author": authors[0].get("family", "") if authors else "",
            "year": issued[0][0],
            "venue": (it.get("container-title") or [""])[0],
            "doi": it.get("DOI", ""),
            "link": it.get("URL", ""),
        })
    return out


def arxiv_candidates(title):
    q = urllib.parse.urlencode({"search_query": 'ti:"%s"' % title, "max_results": 3})
    root = ET.fromstring(get(ARXIV + "?" + q))
    out = []
    for e in root.findall("a:entry", NS):
        names = [(a.findtext("a:name", default="", namespaces=NS)) for a in e.findall("a:author", NS)]
        out.append({
            "source": "arxiv",
            "title": " ".join((e.findtext("a:title", default="", namespaces=NS)).split()),
            "first_author": surname(names[0]) if names else "",
            "year": (e.findtext("a:published", default="", namespaces=NS))[:4],
            "venue": "arXiv",
            "doi": "",
            "link": e.findtext("a:id", default="", namespaces=NS),
        })
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--title", required=True)
    p.add_argument("--author", default="")
    p.add_argument("--year", default="")
    p.add_argument("--doi", default="")
    p.add_argument("--mailto", default="", help="optional email for Crossref polite pool")
    a = p.parse_args()
    want = {"title": a.title, "author": a.author, "year": a.year}

    errors, best = [], None
    for name, fn in (("crossref", lambda: crossref_candidates(a.title, a.author, a.doi, a.mailto)),
                     ("arxiv", lambda: arxiv_candidates(a.title))):
        try:
            for cand in fn():
                verdict, notes = judge(want, cand)
                rank = (verdict == "match", title_ratio(a.title, cand["title"]))
                if best is None or rank > best[0]:
                    best = (rank, verdict, notes, cand)
        except Exception as e:  # network or API problem, reported not hidden
            errors.append("%s: %s" % (name, e))

    if best is None:
        result = {"verdict": "not_found", "errors": errors,
                  "action": "mark [unverified] and tell the user"}
    else:
        _, verdict, notes, cand = best
        result = {"verdict": verdict, "notes": notes, "best_record": cand, "errors": errors}
        if verdict != "match":
            result["action"] = "check by hand, then mark [unverified] if it still fails"
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["verdict"] == "match" else 2)


if __name__ == "__main__":
    main()
