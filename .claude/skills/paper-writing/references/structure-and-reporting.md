# Structure and reporting notes

Adapted from `scientific-writing` (K-Dense-AI/scientific-agent-skills, MIT).

## Evidence binding

Give every source an ID, every claim an ID, and every number an ID in `evidence-ledger.md`. In the draft, mark each factual sentence with its IDs, for example `[C007: S003, S011]`, while drafting. Remove or convert the tags only at the end. One claim per sentence keeps the link clear. If you change a sentence's meaning, check its evidence again.

Search snippets, summaries and another paper's reference list help you find sources. They do not verify a claim. Open the source.

## Never invent

Citations, DOIs, quotations, numbers, sample sizes, units, methods, software versions, approvals, consent statements, funding, conflicts of interest, data or code availability, author roles, AI-use statements. When it is missing, write `[MISSING: ...]`.

## Reporting guidelines by study type

Check the venue's current page for the exact version.

| Study | Guideline |
|---|---|
| Randomised trial | CONSORT (protocol: SPIRIT) |
| Systematic review | PRISMA |
| Observational study | STROBE |
| Diagnostic accuracy | STARD (with AI extension for AI tests) |
| Prediction model | TRIPOD, with AI extension for ML models |
| Case report | CARE |
| Animal study | ARRIVE |
| Quality improvement | SQUIRE |
| Economic evaluation | CHEERS |
| Machine learning paper | Venue reproducibility checklist (for example, NeurIPS or ACL checklists) |

A guideline checklist covers completeness. It does not show the study is good.

## Section purposes

- Abstract: problem, gap, method, main result with a number, limitation or scope. Write last.
- Introduction: the problem, what current work misses, what this paper does, contributions that match the question card.
- Related work: grouped by theme, and ends with how this work differs.
- Method: enough to repeat. Data, split, model, training, evaluation, compute.
- Results: the planned analysis first, then secondary, then exploratory (labelled). Include null and negative results. Same numbers as the results files.
- Discussion: what the results mean within their limits, alternative explanations, concrete limitations, what is left open.
- Conclusion: what was found, at the strength the evidence allows.

Use the venue's structure if it differs. Qualitative and theory papers need not follow this order.

## Consistency checks before handing over

- Same sample sizes, units, denominators, splits and time points in method, results, tables and abstract
- Binary outcomes: report counts with denominators, and say whether an effect is a difference or a ratio. Do not turn one into the other without the baseline.
- Title and abstract match the final text
- Figures and tables match the prose
- Every in-text citation is in the list, and the reverse

## Authorship and disclosure

Authors are responsible for the content. An AI system is not an author. Follow the venue's rule on disclosing AI use, and check what it requires. Do not draft a disclosure from guesses.

## Confidentiality

Do not paste unpublished manuscripts, peer review material, personal data or restricted data into outside services the user did not choose. Keep processing local when unsure.
