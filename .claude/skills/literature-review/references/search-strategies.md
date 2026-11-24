# Search strategies

Adapted from `database_strategies.md` and `search_and_citation.md` in `literature-review` (K-Dense-AI/scientific-agent-skills, MIT). Rewritten for this project.

## Query design

1. Write the inclusion and exclusion criteria before looking at results.
2. Group synonyms with OR, combine concepts with AND. Try known good papers as a pilot: if your query misses papers you already know are relevant, fix the query.
3. Be careful with filters. Language limits, type limits and NOT terms can drop relevant work.
4. Translate the query for each source. Syntax does not carry over (arXiv `ti:` is not a Semantic Scholar operator). Log the query as actually sent.
5. Do not screen by venue, author fame or citation count. Those reflect exposure and age, not quality. Recent and negative results need an equal chance.

## What to record for every search

Query string as sent, source, date and time, filters, the total the source reported, how many you retrieved, and any failure (timeouts, rate limits, capped results). A capped or interrupted retrieval is incomplete, so log it that way.

## arXiv

- Endpoint: `https://export.arxiv.org/api/query`, no key needed
- Fields: `ti:` title, `au:` author, `abs:` abstract, `cat:` category, combined with AND, OR
- Paging with `start` and `max_results`. Wait at least 3 seconds between requests.
- Keep the version number and the dates. A preprint is not peer reviewed.

## Semantic Scholar

- Relevance search: `https://api.semanticscholar.org/graph/v1/paper/search`, plain text query, separate `year` range, `limit` up to 100
- Only about 1000 relevance-ranked results can be reached, so it is not a full export. Split broad topics into several queries.
- Do not invent field operators for this endpoint
- An API key helps with quota. Without one you share a throttled pool, so on HTTP 429 wait and retry later.
- Citation counts and "influential" labels are discovery aids only

## Other sources worth a web search

- OpenAlex (`https://api.openalex.org/works?search=...`) for broad coverage and citation links
- Crossref (`https://api.crossref.org/works/{doi}`) for DOI metadata. A 404 does not prove a DOI from another registrar is fake.
- Venue pages and proceedings (ACL Anthology, OpenReview, NeurIPS, ICML, CVPR), Papers with Code style leaderboards, thesis repositories
- For medicine and biology: PubMed, PMC, bioRxiv, medRxiv. PubMed only pages through the first 10,000 matches, so split large searches.

A web search engine is a fine finder, not a complete index. State that in the limitations.

## Citation chaining

- Backward: read the reference list of the best papers and surveys, then screen those with the same criteria
- Forward: find papers that cite the best ones (Semantic Scholar or OpenAlex citations, or "cited by" on the web)
- Log the seed papers, how many were found, and what was kept
- Link a preprint, its journal version and any follow-up to one study so it is counted once

## Reading depth

Record `full text` or `abstract only` for each paper. Never describe a method or number you did not read. Search snippets and machine summaries are leads.

## Verify, then trust

A real DOI shows the paper exists. It does not show the paper supports your sentence. Check title, authors, year, version, correction or retraction notices, and find the passage that backs the claim. Citations without a DOI need a manual check. A failed lookup caused by a timeout is not proof of a fake reference. Retry, then mark `[unverified]`.
