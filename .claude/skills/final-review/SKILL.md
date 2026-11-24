---
name: final-review
description: Stage 7 of a research project. Use when a paper draft exists and the user wants it checked before submission or sharing: claims against evidence, citation accuracy, numbers, consistency, structure, and writing quality. Reviews and reports problems, does not rewrite the whole paper.
---

# Final review

Goal: find what a tough reviewer would find, before a real reviewer does.

## Checks, in order

1. **Claims vs evidence.** List every claim in the abstract, introduction and conclusion. For each, point to the table, figure or reference that supports it. Flag any claim with no support or stronger wording than the data allows.
2. **Numbers.** Compare every number in the text against `05-results.md` and the raw files in `results/`. List mismatches.
3. **Citations.** For each reference, confirm it exists by searching for its title (arXiv, Semantic Scholar, or web search). Check authors, year and venue. Flag anything that cannot be found, and any in-text citation missing from the reference list or the reverse.
4. **Consistency.** Same terms, same notation, same dataset names, same numbers in the abstract, body and conclusion. Research question and hypotheses match what was tested.
5. **Structure.** Does each section do its job? Is anything repeated? Is the contribution statement honest?
6. **Reviewer simulation.** Write the 5 hardest questions a reviewer would ask, and the 3 most likely reasons for rejection. Suggest how to address each.
7. **Writing quality.** Mark unclear sentences, filler, hype, and AI-sounding phrasing. Give examples and fixes, not a full rewrite.
8. **Ethics and reproducibility.** Data licences, consent, code and data availability, seeds and versions.

## Output file

Save to `research/<project-slug>/07-review.md` with a prioritised list: must fix, should fix, nice to have. Include the location of each problem.

## Rules

- Be honest and specific. A review that only says the paper is good is useless.
- Do not change the paper unless the user asks. Report first, then offer to apply fixes.
- Never mark a citation as verified unless you found it in a search in this session.
