# Review checklist

Adapted from `paper-self-review` and `citation-verification` (Galaxy-Dawn/claude-scholar, MIT), `peer-review` (K-Dense-AI/scientific-agent-skills, MIT) and `paper-check` (fcakyon/phd-skills, MIT).

## Comment format

Every major or minor comment has five parts:
- Location (section, paragraph, table, figure)
- What you observed
- The criterion or evidence behind the concern
- Why it matters
- What to do about it

Ask for new work only when it is needed to support a central claim, and keep it small. Offer narrowing the claim, adding uncertainty, labelling something exploratory or a sensitivity check when that is enough.

Do not write "not reported" as "wrong". Separate these:
- Not reported: the paper does not give enough to judge
- Possible design or analysis problem: the method may not answer the question
- Demonstrated inconsistency: two places in the paper or files disagree
- Integrity concern: describe neutrally, and leave it for the author or editor

## Claim and evidence

Common mismatches:
- causal wording from an observational design
- mechanism claimed from association or prediction alone
- a secondary or exploratory result presented as the main finding
- the direction is right but the size or precision is overstated
- extrapolation to other populations, tasks, models or time
- "no effect", "equivalent" or "safe" from an imprecise or non-significant result
- abstract or conclusion leaves out harms, null results, or limits seen in the body
- novelty claimed beyond what the search covers

Response: name the claim, name the result or missing evidence, explain the gap, ask for narrower wording or the missing analysis.

## Design and unit

- Are repeated measures, seeds, folds, images or samples from the same source treated as independent
- Are train and test truly separate (see the leakage list in methodology-design)
- Was tuning budget equal across methods
- Is the primary metric the one fixed in advance
- Does the analysis match the design (pairing, clustering)
- Is there a size or precision rationale
- Are there ablations that test the stated mechanism

## Statistics

- Test fits the question and the data, with assumptions checked
- Effect sizes and intervals given, not only p-values
- Multiple comparisons handled
- No observed power
- Failed runs and exclusions disclosed

## Reproducibility

Data source and version, preprocessing order, code, environment and versions, seeds, hyperparameters, compute, and what is restricted and why. Do not say a result was reproduced unless the code was run with documented commands.

## Citations

Match on title (close), first author, year (within one), venue. Check order: DOI or publisher page, arXiv, Crossref, Semantic Scholar. Search engines and Google Scholar are fine for finding a source but weaker as proof of a citation. Then confirm the source supports the sentence it sits under. Mark anything not matched as unverified, never as fine.

## Figures and tables

Same numbers as the text, units, denominators, uncertainty, readable at final size, accessible colours, a caption that stands alone.

## Reviewer simulation

Write as a skeptical reviewer in the field: five hardest questions, three most likely reasons to reject, what is missing (baselines, ablations, datasets, statistics), and a fix or a response for each.

## Readiness verdict

- Ready: no blocking issues, minor fixes only
- Ready after fixes: list the blocking fixes
- Not ready: a central claim lacks support, or the method or numbers cannot be trusted

The author decides when to submit. The verdict supports that choice.

## Tone

Be fair, specific and kind. Criticise the work, not the person. Do not overstate certainty about things you could not check.
