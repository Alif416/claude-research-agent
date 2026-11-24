---
name: methodology-design
description: "Stage 4 of a research project. Use when the user has a research question card and needs a reproducible plan: unit of analysis, data, method, fair baselines, metrics, sample size or number of runs, ablations, leakage and confound checks, and a pre-registered analysis plan. Not for running the experiments."
---

# Methodology design

Goal: a plan another person could follow and repeat, sized to the user's real compute and time, written before any result is seen.

> Adapted from `experimental-design` and `statistical-power` (K-Dense-AI/scientific-agent-skills, MIT), the ablation planning idea in `experiment-design` (fcakyon/phd-skills, MIT) and the method-selection step in `research-ideation` (Galaxy-Dawn/claude-scholar, MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## Inputs

Read `03-research-question.md` and the comparison matrix in `02-literature-review.md`. Ask for limits if unknown: compute, time, language and tools, data already held.

## Steps

1. **Fix the unit.** State the question, the unit of analysis, and the response or metric. The unit is where independence holds. Repeated rows from the same subject, fold, window or seed are not independent samples, and treating them as independent (pseudoreplication) is the most common fatal error. Replicate at the level where things are randomised or split.
2. **Data.** For each dataset give name, source link, size, licence, and known problems. Search to confirm it exists. If data must be collected, outline how, and raise consent and ethics. State the split plan and where leakage could creep in (duplicate items across splits, time leakage, preprocessing fitted on all data, target-derived features).
3. **Method.** Describe the approach in plain steps and why it fits the mechanism in the question card. Name the nearest published method it builds on, with its ledger ID.
4. **Baselines.** At least one simple baseline and one strong published method. Give every method the same tuning budget and the same data. An under-tuned baseline makes any result meaningless.
5. **Metrics and comparison.** For each metric say what it measures and why it answers the question. Fix the primary metric and its direction now. State the comparison plan: number of seeds or folds, the interval to report, the statistical test and its assumptions, a non-parametric fallback, the effect size, and any multiple-comparison correction.
6. **Size it.** Estimate sample size or number of runs needed to detect the effect you care about. If you cannot reach it, say what the study can and cannot show.
7. **Ablations.** Choose the few that test each hypothesis directly, and say what result would count against it. Skip decorative ablations.
8. **Threats to validity.** List leakage, confounds (batch, day, operator, dataset artefacts), small samples, metric limits, unfair baselines, and how each is handled.
9. **Plan before results.** Write the analysis plan now: primary comparison, secondary comparisons, exclusions, stopping rule. Anything done after seeing results must be labelled exploratory. Keep a deviations log.
10. **Work plan.** Ordered tasks with rough time. The first task is the smallest experiment that could show whether the idea has any signal at all.

## Reference files

- `references/design-and-power.md`: unit and pseudoreplication, leakage checklist, fair baselines, choosing an effect size, sample size and runs, controls, reproducibility records
- `templates/analysis-plan.md`: copy it to the top of `04-methodology.md` and fill it before any result exists
## Decisions

When the user chooses between options (a method, a baseline, a smaller scope, a number of runs), record each choice with its reason in a **Decision** section at the top of `04-methodology.md`, and make the plan match it. If they overrule a recommendation, say so there.

## Output

Save `research/<project-slug>/04-methodology.md`. Include a one-page analysis plan at the top and a deviations log section that stays empty until Stage 5.

## Rules

- Only cite datasets and tools you confirmed exist.
- Design only what the user can run. Offer a smaller version if needed.
- Define everything that affects results: splits, seeds, hyperparameter ranges, preprocessing order.
- Do not choose a method because it is fashionable. Choose it because it answers the question.
