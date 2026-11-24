---
name: final-review
description: Stage 7 of a research project. Use when a draft exists and the user wants it checked before submission or sharing. Audits every claim against evidence, verifies numbers against result files, verifies citations, simulates a tough reviewer, and gives a prioritised readiness verdict. Reports problems, does not rewrite the paper.
---

# Final review

Goal: find what a tough reviewer would find, before a real reviewer does.

> Adapted from `paper-self-review` and `citation-verification` (Galaxy-Dawn/claude-scholar, MIT), `peer-review` (K-Dense-AI/scientific-agent-skills, MIT) and `paper-check` (fcakyon/phd-skills, MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## Checks, in order

1. **Claim audit.** List every claim in the abstract, introduction and conclusion. For each, fill this entry:
   - Claim
   - Verdict: keep, weaken, revise or remove
   - Evidence used (ledger ID, table or figure)
   - Missing evidence
   - Overclaim risk
   - Suggested wording
2. **Numbers.** Compare every number in the text with `results/` and `05-results.md`. List each mismatch with its location. Check that the abstract, tables and conclusion agree with each other.
3. **Citations.** For each reference, run `../literature-review/scripts/verify_citation.py` or check by hand. Use the matching rules: title matches, first author matches, year within one, venue correct. Check in this order: DOI or publisher page, arXiv, Crossref, Semantic Scholar. A search engine finds papers but is weak proof that a citation is right. Then check the other direction: every in-text citation is in the list and the reverse. For key claims, open the source and confirm it says what the paper says it does. Mark anything unverified.
4. **Consistency.** Same terms, notation, dataset names and numbers throughout. The research question and hypotheses match what was tested. Deviations from the methodology plan are disclosed.
5. **Structure.** The abstract has problem, method, results and contributions. The method is detailed enough to reproduce. Results support the conclusions. The discussion states limitations. Nothing is repeated without reason.
6. **Figures and tables.** Each has a clear caption, supports the text, is readable, and meets the venue's format.
7. **Reviewer simulation.** Write the five hardest questions a reviewer would ask and the three most likely reasons for rejection. For each, say what to change or add. Include missing baselines, ablations that were not run, and unclear statistics.
8. **Writing quality.** Mark unclear sentences, filler, hype, and AI-sounding phrasing, with examples and fixes. Do not rewrite the whole paper.
9. **Ethics, disclosure and reproducibility.** Data licences and consent, AI-use disclosure the venue requires, code and data availability, seeds and versions.

## Reference files

`references/review-checklist.md` has the comment format, claim and evidence mismatches, design and statistics checks, citation matching, the reviewer simulation prompt and the verdict definitions.
## Decisions

After the review, ask the user what they will fix, what they will leave, and why. Record this in a **Decision** section at the top of `07-review.md`, next to the readiness verdict. The author decides when to submit.

## Output

Save `research/<project-slug>/07-review.md`:

- **Readiness verdict:** ready, ready after fixes, or not ready, with the blocking issues named first
- Prioritised list: must fix, should fix, nice to have, each with its location
- Claim audit table
- Number mismatches
- Citation check results
- Reviewer questions and likely rejection reasons

## Rules

- Be honest and specific. A review that only says the paper is good is useless.
- Report first. Change the paper only if the user asks.
- A valid reference does not prove the claim it is attached to. Check the claim.
- Never mark a citation verified unless you matched it in a search result in this session.
- This stage supports the author's judgement. The author decides whether the paper is ready to submit.
