#!/usr/bin/env python3
"""Style lint for research drafts. Flags patterns that make prose read as machine written.

Standard library only. Offline. Reads a Markdown or text file and prints findings
with line numbers and rule IDs. It does not rewrite anything, and it cannot judge
whether the writing is good or whether the science is right.

Usage:
    python3 lint_style.py draft.md
    python3 lint_style.py draft.md --json

Exit codes: 0 no findings, 1 findings reported, 2 bad input.

Adapted from the pattern lists in `writing-anti-ai` (Galaxy-Dawn/claude-scholar, MIT),
which draws on Wikipedia's "Signs of AI writing" guide. Rule set rewritten for this project.
"""
import argparse
import json
import re
import statistics
import sys

BANNED_WORDS = [
    "delve", "delves", "delving", "tapestry", "landscape", "intricate", "intricacies",
    "pivotal", "underscore", "underscores", "underscoring", "foster", "fosters", "fostering",
    "leverage", "leverages", "leveraging", "showcase", "showcases", "showcasing",
    "testament", "vibrant", "crucial", "paramount", "multifaceted", "seamless", "seamlessly",
    "groundbreaking", "cutting-edge", "state-of-the-art", "novel", "robust", "comprehensive",
    "holistic", "realm", "myriad", "plethora", "endeavor", "embark", "unlock", "harness",
]

FILLER_PHRASES = [
    "it is important to note", "it is worth noting", "it should be noted",
    "it is worth mentioning", "due to the fact that", "in order to",
    "in today's rapidly evolving", "plays a crucial role", "plays a key role",
    "plays a vital role", "a wide range of", "has the potential to", "serves as",
    "stands as", "in the realm of", "at the end of the day", "a testament to",
    "paves the way", "sheds light on", "in the context of",
]

TRANSITION_OPENERS = [
    "moreover", "additionally", "furthermore", "in addition", "consequently",
    "notably", "importantly", "interestingly", "ultimately",
]

SUMMARY_ENDERS = ["overall,", "in summary,", "in conclusion,", "ultimately,", "together,", "taken together,", "in short,"]

HEDGES = ["may", "might", "could", "potentially", "possibly", "perhaps", "somewhat", "arguably", "seemingly", "appears to", "seems to"]

ING_TAIL = re.compile(
    r",\s+(highlighting|underscoring|ensuring|showcasing|emphasizing|emphasising|demonstrating|"
    r"reflecting|fostering|enabling|paving|contributing to|illustrating)\b", re.I)
NEG_PARALLEL = re.compile(r"\bnot (just|only|merely) [^.;]{1,80}?,? (but|it'?s|it is)\b", re.I)
DASH = re.compile(r"—|(?<=\s)--(?=\s)|(?<=\s)–(?=\s)")
TAG = re.compile(r"\[(?:C|S|N)\d+[^\]]*\]")


def clean_lines(text):
    """Return list of (lineno, text) with code blocks, front matter, tables and ID tags blanked."""
    out, in_code, in_front = [], False, False
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if i == 1 and s == "---":
            in_front = True
            out.append((i, ""))
            continue
        if in_front:
            if s == "---":
                in_front = False
            out.append((i, ""))
            continue
        if s.startswith("```"):
            in_code = not in_code
            out.append((i, ""))
            continue
        if in_code or s.startswith("|") or s.startswith("#"):
            out.append((i, ""))
            continue
        out.append((i, TAG.sub("", line)))
    return out


def paragraphs(lines):
    """Group consecutive non-empty lines. Returns list of (start_lineno, text)."""
    paras, buf, start = [], [], None
    for no, t in lines:
        if t.strip():
            if not buf:
                start = no
            buf.append(t.strip())
        elif buf:
            paras.append((start, " ".join(buf)))
            buf = []
    if buf:
        paras.append((start, " ".join(buf)))
    return paras


def sentences(par):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])", par)
    return [p.strip() for p in parts if len(p.split()) >= 3]


def run(text):
    findings = []

    def add(rule, line, msg, snippet=""):
        findings.append({"rule": rule, "line": line, "message": msg, "match": snippet[:80]})

    lines = clean_lines(text)

    for no, t in lines:
        low = t.lower()
        if not t.strip():
            continue
        if DASH.search(t):
            add("S01", no, "Dash used as punctuation. Use a comma, period or parentheses.", DASH.search(t).group(0))
        for w in BANNED_WORDS:
            m = re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", low)
            if m:
                add("S02", no, "Stock word. Use a plain word or give the specific fact.", w)
        for p in FILLER_PHRASES:
            if p in low:
                add("S03", no, "Filler phrase. Cut it or say the concrete thing.", p)
        if NEG_PARALLEL.search(t):
            add("S04", no, "Negative parallelism ('not just X but Y'). State Y directly.", NEG_PARALLEL.search(t).group(0))
        if ING_TAIL.search(t):
            add("S05", no, "Tacked-on -ing phrase. Cut it or turn it into a sentence with a fact.", ING_TAIL.search(t).group(0).strip(", "))

    paras = paragraphs(lines)

    # S06 transition openers: count per document and consecutive use
    openers = []
    for start, par in paras:
        first = par.lower().split(" ", 1)[0].strip(",")
        openers.append(first if first in TRANSITION_OPENERS else None)
    n_open = sum(1 for o in openers if o)
    for idx, (start, par) in enumerate(paras):
        if openers[idx] and idx > 0 and openers[idx - 1]:
            add("S06", start, "Consecutive paragraphs open with a transition word.", openers[idx])
    if n_open > max(2, len(paras) // 6):
        add("S06", paras[0][0] if paras else 1,
            f"{n_open} of {len(paras)} paragraphs open with a transition word. Drop most of them.", "")

    # S07 uniform sentence length inside a paragraph
    for start, par in paras:
        ss = sentences(par)
        if len(ss) >= 4:
            lens = [len(s.split()) for s in ss]
            mean = statistics.mean(lens)
            if mean > 0 and statistics.pstdev(lens) / mean < 0.22:
                add("S07", start, f"Sentences are nearly the same length (about {round(mean)} words). Vary the rhythm.", "")

    # S08 neat summary closers
    closers = []
    for start, par in paras:
        ss = sentences(par)
        if ss and any(ss[-1].lower().startswith(e) for e in SUMMARY_ENDERS):
            closers.append(start)
    if len(closers) >= 3:
        for ln in closers:
            add("S08", ln, "Paragraph ends on a summary line. Several do. End on the last real point.", "")

    # S09 stacked hedges inside one sentence
    for start, par in paras:
        for s in sentences(par):
            low = s.lower()
            hits = [h for h in HEDGES if re.search(r"\b" + re.escape(h) + r"\b", low)]
            if len(hits) >= 2:
                add("S09", start, "Stacked hedges in one sentence. Hedge once, at the claim.", ", ".join(hits))

    # S10 repeated sentence starts
    for start, par in paras:
        ss = sentences(par)
        firsts = [" ".join(s.split()[:2]).lower() for s in ss]
        for f in set(firsts):
            if firsts.count(f) >= 3:
                add("S10", start, "Three or more sentences in one paragraph start the same way.", f)

    return findings, len(paras)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true", help="print findings as JSON")
    a = ap.parse_args()
    try:
        with open(a.file, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if len(text) > 2_000_000:
        print("error: file too large", file=sys.stderr)
        return 2
    findings, n_par = run(text)
    findings.sort(key=lambda x: (x["line"], x["rule"]))
    if a.json:
        print(json.dumps({"paragraphs": n_par, "count": len(findings), "findings": findings}, indent=2))
    else:
        for f in findings:
            m = f" [{f['match']}]" if f["match"] else ""
            print(f"line {f['line']}: {f['rule']} {f['message']}{m}")
        print(f"\n{len(findings)} finding(s) in {n_par} paragraph(s).")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
