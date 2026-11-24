---
name: analysis-and-results
description: Stage 5 of a research project. Use when the user wants to run the planned experiments or analysis and get strict, honest results: validated inputs, locked comparisons, statistics with intervals, tests and effect sizes, real figures, and claim candidates with allowed wording. Has a read-only audit mode. Does not write the paper's Results section.
---

# Analysis and results

Goal: results that are correct, repeatable, and reported with exactly the strength the evidence allows.

> Adapted from `results-analysis` (Galaxy-Dawn/claude-scholar, MIT), `statistical-analysis` (K-Dense-AI/scientific-agent-skills, MIT) and the baseline comparison idea in `compare` (fcakyon/phd-skills, MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## Modes

- **Full mode** (default): run the analysis and write the whole bundle.
- **Audit mode**: use when the user asks for a review, a dry run, or when core evidence is missing. Create no files or figures. Report which statistics are valid, which are not, what is missing, and what claims could be made at most.

## Steps

1. **Set up.** Work in `research/<project-slug>/code/` with a README, a requirements file, fixed seeds and one script per experiment. Save raw output in `results/` as CSV or JSON.
2. **Validate inputs.** List metric tables, logs, seeds, baselines, ablations and protocol notes. Check metric direction, the unit of analysis, run and seed counts, missing or failed values, and whether methods are comparable. Stop and report if the comparison is not statistically valid.
3. **Run the smallest experiment first** (from the work plan). If it shows no signal, tell the user before scaling up.
4. **Read the output.** If results look wrong (perfect scores, identical numbers across seeds, a loss that never moves), treat it as a bug and investigate before reporting anything.
5. **Lock the comparisons.** Before computing any statistic, write down which method is compared to which baseline, the primary metric, the unit, and which findings would change a decision. Do not merge unrelated comparisons.
6. **Run strict statistics.** Report: mean and spread, a 95% interval (or another justified one), the number of runs and seeds, the test with its assumptions checked and a non-parametric fallback, effect sizes for the main contrasts, and a multiple-comparison correction when several are reported. Never report only the best score or only a p-value.
7. **Make real figures from the result files.** A non-trivial analysis needs one main comparison figure, one supporting figure (training curves, ablation, error breakdown) and one exact numeric table. Each major figure must answer: why it exists, what the reader should notice, and what that changes in belief or next steps. A figure that cannot answer the third question is decoration.
8. **Claim candidates.** For each, write: the claim, the evidence (file and number), allowed wording, forbidden stronger wording, uncertainty, the next check, and a decision (keep, weaken, revise, discard). Add the numbers and claims to `evidence-ledger.md`.
9. **Final check.** Primary question explicit, sample sizes stated, tests justified, effect sizes given, figures real, limits written down, no claim stronger than its evidence. Compare what was run against `04-methodology.md` and log every deviation with the reason.

## Reference files

`references/statistics-guide.md` has the test table, effect sizes, intervals, how to word claims about no effect, multiple comparisons, an audit mode checklist, the claim candidate entry with an example, and figure rules. Read it before step 5.
## Decisions

When the user decides what to do with a claim candidate (keep, weaken, revise, discard) or how to handle a deviation, write it in a **Decision** section at the top of `05-results.md` and update the claim row in the ledger. The paper stage must use the decided wording.

## Output

Save `research/<project-slug>/05-results.md` (question, key findings, best-supported comparisons, caveats, claim candidates, deviations) with a `stats-appendix` section (tests, assumptions, effect sizes, intervals, corrections) and a `figure catalog` section (file, purpose, data source, caption needs, key observation). Do not write a manuscript-style Results section here. That belongs to the paper-writing stage.

## Rules

- Never fabricate, round up or adjust a number. Missing seeds, sample sizes or raw metrics are blockers, and you report them as blockers.
- No comparable baseline means no significance claim. An unclear unit of analysis blocks winner claims.
- Never compute observed power, and never read a non-significant test as proof of no effect or equality. Say what the interval allows.
- Never tune on the test set. If asked, explain that it would invalidate the result.
- A statistics file whose interpretation contradicts its own test, unit or comparison set is set aside until its source is checked.
- If compute is not available here, write the code and run instructions, and say clearly that nothing was executed.
