---
name: literature-review
description: Stage 2 of a research project. Use when the user wants a literature review on a chosen topic. Runs a recorded multi-database search (arXiv, Semantic Scholar, web), de-duplicates, screens with counts, extracts into a comparison matrix, writes a thematic synthesis, and verifies every citation. Not for choosing a topic.
---

# Literature review

Goal: a review the user can trust, built only from papers that were found and checked, organised by theme and not paper by paper.

> Adapted from `literature-review` (K-Dense-AI/scientific-agent-skills, MIT, v1.11), `literature-triage-matrix` (WenyuChiou/research-hub, MIT) and the `literature-reviewer` agent approach in Galaxy-Dawn/claude-scholar (MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## Tools

Scripts are in `scripts/` (Python standard library only):

```bash
python3 scripts/search_arxiv.py "query" --max 15
python3 scripts/search_semantic_scholar.py "query" --max 15 --year 2021-
python3 scripts/verify_citation.py --title "..." --author "Surname" --year 2023
```

Use WebSearch for what these miss: journals, theses, dataset pages, benchmark leaderboards. Copy `templates/evidence-ledger.md` to `research/<project-slug>/evidence-ledger.md` if it does not exist.

## Phases

1. **Plan.** Confirm the topic or research question, year range, field, target count (default 25 to 40 kept papers), and review style: narrative, scoping, or systematic-style with counts. Write inclusion and exclusion criteria before searching.
2. **Search.** Write 5 to 10 queries (synonyms, method names, application names). Run each in at least two sources. Include preprints. Log every query string, source, date and result count in the output file. A single-database or undocumented search is the most common failure, so do not skip this.
3. **De-duplicate.** Match on title and year. Link a preprint and its published version to one record so one study is not counted twice.
4. **Screen.** Title and abstract first, then full text for the likely keepers. Keep counts: found, after de-duplication, after screening, kept. Note why borderline papers were dropped.
5. **Extract and compare.** For every kept paper fill one row of the matrix: problem, method, data, main result, limitation, quality note, and reading depth (`full text` or `abstract only`). Read at least the 10 to 15 most relevant papers in full when they are open access.
6. **Synthesise.** Group into 3 to 6 themes. For each theme say what is established, where papers disagree, and what is weak or missing. Never write a paper-by-paper list. End with a gaps section that hands off to the research-question stage.
7. **Verify and log.** Run `verify_citation.py` for every reference, or check by hand with the matching rules below. Record each source in the evidence ledger with an ID (S1, S2, ...), its status, and the reading depth. Add the key claims you rely on as claim rows (C1, C2, ...) pointing to source IDs.

## Matching rules for citation checks

Title matches ignoring case and small punctuation. First author surname must match. Year may differ by one (preprint versus published). Venue must be correct if stated. Check in this order: DOI or publisher page, arXiv, Crossref, Semantic Scholar. A valid DOI proves the paper exists, not that it supports your claim, so for any specific finding also locate it in the text and note the section.

If a check fails: try other keywords and sources once, then mark `[unverified]` and tell the user. Never fill gaps with guessed details.

## Reference files

`references/search-strategies.md` has query design rules, what to log, source-specific limits (arXiv, Semantic Scholar, OpenAlex, Crossref), citation chaining, and the verify-then-trust rule. Read it before phase 2.
## Output

Save `research/<project-slug>/02-literature-review.md` with: scope and criteria, search log, counts, comparison matrix, thematic synthesis, gaps, reference list. Plus the updated `evidence-ledger.md`.

## Rules

- Never cite a paper you did not find through a tool in this session.
- Never state a number unless it came from text you read. If you read only the abstract, say so.
- Web search cannot show that coverage is exhaustive. Say that in the limitations.
- Do not skip quality notes: peer reviewed or preprint, sample size, dataset, obvious bias.
- Paraphrase. Keep any direct quote short and in quotation marks.
- Flag outdated searches: if the newest paper is more than a few months old, say the search date.
