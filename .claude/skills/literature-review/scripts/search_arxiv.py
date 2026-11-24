#!/usr/bin/env python3
"""Search arXiv and print one JSON object per line.

Usage:
    python3 search_arxiv.py "query words" [--max 15] [--sort relevance|date]
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}


def fetch(url, retries=3):
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


def clean(text):
    return " ".join((text or "").split())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("query")
    p.add_argument("--max", type=int, default=15)
    p.add_argument("--sort", choices=["relevance", "date"], default="relevance")
    args = p.parse_args()

    sort = "relevance" if args.sort == "relevance" else "submittedDate"
    params = urllib.parse.urlencode({
        "search_query": "all:" + args.query,
        "start": 0,
        "max_results": args.max,
        "sortBy": sort,
        "sortOrder": "descending",
    })
    try:
        data = fetch(API + "?" + params)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

    root = ET.fromstring(data)
    count = 0
    for entry in root.findall("a:entry", NS):
        link = clean(entry.findtext("a:id", default="", namespaces=NS))
        published = clean(entry.findtext("a:published", default="", namespaces=NS))
        item = {
            "source": "arxiv",
            "title": clean(entry.findtext("a:title", default="", namespaces=NS)),
            "authors": [clean(a.findtext("a:name", default="", namespaces=NS))
                        for a in entry.findall("a:author", NS)],
            "year": published[:4],
            "abstract": clean(entry.findtext("a:summary", default="", namespaces=NS)),
            "link": link,
            "pdf": link.replace("/abs/", "/pdf/") if "/abs/" in link else "",
        }
        print(json.dumps(item, ensure_ascii=False))
        count += 1
    if count == 0:
        print(json.dumps({"note": "no results"}), file=sys.stderr)


if __name__ == "__main__":
    main()
