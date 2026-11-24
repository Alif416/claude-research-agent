#!/usr/bin/env python3
"""Search Semantic Scholar and print one JSON object per line.

Usage:
    python3 search_semantic_scholar.py "query words" [--max 15] [--year 2021-]

Set S2_API_KEY in the environment for higher rate limits (optional).
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,year,authors,abstract,citationCount,venue,externalIds,url,openAccessPdf"


def fetch(url, retries=4):
    headers = {"User-Agent": "research-agent/1.0"}
    key = os.environ.get("S2_API_KEY")
    if key:
        headers["x-api-key"] = key
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise


def main():
    p = argparse.ArgumentParser()
    p.add_argument("query")
    p.add_argument("--max", type=int, default=15)
    p.add_argument("--year", help="e.g. 2021-  or  2019-2024")
    args = p.parse_args()

    params = {"query": args.query, "limit": min(args.max, 100), "fields": FIELDS}
    if args.year:
        params["year"] = args.year
    url = API + "?" + urllib.parse.urlencode(params)

    try:
        data = fetch(url)
    except urllib.error.HTTPError as e:
        print(json.dumps({"error": "HTTP %s" % e.code}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

    papers = data.get("data") or []
    if not papers:
        print(json.dumps({"note": "no results"}), file=sys.stderr)
    for r in papers:
        ext = r.get("externalIds") or {}
        pdf = (r.get("openAccessPdf") or {}).get("url", "")
        item = {
            "source": "semantic_scholar",
            "title": r.get("title", ""),
            "authors": [a.get("name", "") for a in r.get("authors") or []],
            "year": r.get("year"),
            "venue": r.get("venue", ""),
            "citations": r.get("citationCount"),
            "abstract": " ".join((r.get("abstract") or "").split()),
            "doi": ext.get("DOI", ""),
            "arxiv": ext.get("ArXiv", ""),
            "link": r.get("url", ""),
            "pdf": pdf,
        }
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
