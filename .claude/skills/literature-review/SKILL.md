---
name: literature-review
description: Stage 2 of a research project. Use when the user wants a literature review on a chosen topic. Searches arXiv, Semantic Scholar and the web, screens papers, extracts key points, and writes a structured synthesis with verified citations. Not for picking a topic.
---

# Literature review

Goal: a review the user can trust, built only from papers that were actually found and checked.

## Tools in this skill

Two scripts live in `scripts/` next to this file. They use only the Python standard library.

```bash
python3 scripts/search_arxiv.py "federated learning remote patient monitoring" --max 15
python3 scripts/search_semantic_scholar.py "federated learning remote patient monitoring" --max 15 --year 2021-
```

Both print JSON lines with title, authors, year, venue, abstract, link and (for Semantic Scholar) citation count. Semantic Scholar rate limits anonymous use. If you hit a 429, wait and retry, or ask the user to set the `S2_API_KEY` environment variable.

Use WebSearch to find things the two sources miss: journal papers, theses, dataset pages, benchmark leaderboards.

## Steps

1. **Confirm scope.** Topic or research question, year range, field, rough number of papers wanted (default 25 to 40), and review style (narrative, thematic, or systematic-style table).
2. **Search broadly.** Write 5 to 10 different queries (synonyms, method names, application names). Run each through arXiv and Semantic Scholar. Keep a log of queries in the output file so the search can be repeated.
3. **Collect and de-duplicate.** Same paper often appears in both. Match on title and year.
4. **Screen.** Keep papers that are on topic, recent enough or foundational, and have a real abstract. Note why borderline papers were dropped. Aim for quality over count.
5. **Read.** For the 10 to 15 most relevant papers, fetch the abstract page or PDF with WebFetch and extract: problem, method, data, results, limitations. If you could only read the abstract, say "abstract only" in your notes.
6. **Group.** Sort papers into 3 to 6 themes (by method, by problem setting, or by time). Do not just list papers one after another.
7. **Synthesise.** For each theme, say what is established, where papers disagree, and what is weak or missing. End with a short "gaps" section that points to the research question stage.
8. **Verify citations.** Every paper in the final text must have a title, authors, year and link taken from a search result. Run a last pass that matches each citation against your search log. Remove or mark `[unverified]` anything that fails.

## Output file

Save to `research/<project-slug>/02-literature-review.md` with these sections: scope and search log, selection summary (found, screened, kept), thematic review, comparison table (paper, method, data, result, limitation), gaps, reference list.

## Rules

- Never cite a paper you did not find through a tool in this session.
- Never state a result number unless it came from the paper text you read.
- Do not copy long passages from papers. Paraphrase, and keep any direct quote very short and in quotation marks.
- Say clearly when the evidence is thin or when you only saw abstracts.
