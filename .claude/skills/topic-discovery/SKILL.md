---
name: topic-discovery
description: Stage 1 of a research project. Use when the user gives a broad research area and wants help finding a specific, publishable topic inside it. Finds recent work, spots open gaps, and proposes a short list of candidate topics with a novelty check. Not for reviewing literature in depth.
---

# Topic discovery

Goal: go from a broad area to 3 to 5 concrete candidate topics, and help the user pick one.

## Before you search

Ask the user, only if not already clear:
- The area, and any sub-area they prefer
- Their constraints: time available, compute, data access, programming skills
- What the work is for: course project, thesis, conference paper, journal paper
- Anything they have already tried or want to avoid

## Steps

1. **Map the area.** Run 4 to 6 web searches and use the literature-review scripts (`search_arxiv.py`, `search_semantic_scholar.py` in the literature-review skill folder) to find survey papers and the most cited recent papers from the last 3 years. Surveys are the fastest way to see the structure of a field.
2. **Find the open edges.** Look for "future work" and "limitations" sections in the best recent papers, open challenges listed in surveys, and areas with many papers on method but few on evaluation (or the reverse).
3. **Draft candidate topics.** For each one, write: a one-line title, why it matters, the gap it fills, what data or tools it needs, and a rough effort estimate (low, medium, high).
4. **Novelty check.** For each candidate, search for the exact idea in plain words. Record the 2 or 3 closest existing papers and say how the candidate differs. If something almost identical already exists, say so and drop or reshape the candidate.
5. **Fit check.** Score each candidate against the user's constraints (feasible, stretch, not realistic).
6. **Recommend.** Name your top pick and say why in 3 or 4 sentences. Be honest about the risks.

## Output file

Save to `research/<project-slug>/01-topic.md` with: area, constraints, candidate table, novelty notes with links, recommendation.

## Rules

- Every paper you mention needs a link you actually saw in a search result.
- Do not call a topic novel unless you searched for it. Say "I found no close match in these searches" rather than "nobody has done this".
- Prefer topics the user can finish. A smaller topic done well beats a big one left half done.
