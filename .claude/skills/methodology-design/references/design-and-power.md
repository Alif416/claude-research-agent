# Design, power and leakage notes

Adapted from `experimental-design`, `statistical-power` and `statistical-analysis` (K-Dense-AI/scientific-agent-skills, MIT) and `experiment-design` (fcakyon/phd-skills, MIT).

## Unit of analysis and pseudoreplication

The unit is the thing that was independently assigned or sampled. Ask of every table row: if I took the next row, would it carry new independent information?

Common traps:
- several seeds of one trained model treated as independent datasets
- many windows or frames from the same subject or recording split across train and test
- several measurements per cell, image, patient, site or operator analysed as separate samples
- cross-validation folds from the same group treated as independent samples in a test

Fix: split and replicate at the group level, and analyse at the same level, or use a model that represents the dependence. State the unit in the analysis plan.

## Leakage checklist

- duplicates or near-duplicates across train, validation and test
- time order broken (future data in training)
- group overlap across splits (same subject, same source document, same repository)
- preprocessing fitted on all data before the split (scaling, feature selection, vocabulary, imputation)
- features derived from the target or from information not available at prediction time
- hyperparameters or early stopping chosen on the test set
- pretrained model that has seen the test data

## Baselines and fairness

One simple baseline, one strong published baseline, and the user's method. Same data, same split, same tuning budget, same compute. Say how many trials each method got. A weak or untuned baseline makes the gain meaningless.

## Choosing the effect size for planning

Do not invent a number. In order of preference:
1. The smallest effect that would change a decision or matter (smallest effect of interest)
2. An estimate from a pilot or a prior paper, with its uncertainty and with the thought that published effects tend to be inflated
3. A convention such as small, medium or large, only as a last resort and labelled so

Always show a sensitivity range: required n across several plausible effect sizes. One number hides the largest uncertainty.

## Sample size and runs

- Inputs: effect size, spread, significance level, power (often 80%), allocation ratio, design
- Two-sided is the default. Justify one-sided.
- Inflate for loss: `n_enrolled = ceil(n_analysed / (1 - dropout_rate))`. A 20% loss means 25% more.
- Clustered data: a rough design effect is `1 + (m - 1) * ICC` for equal clusters of size m. Treat it as a planning guess. With unequal or few clusters, simulate.
- Multiple primary comparisons: power each at the corrected alpha, or simulate the whole procedure.
- Machine learning: seeds and folds give precision, not independence. Decide the number of seeds from the spread you saw in a pilot, and report intervals.
- If simulation is used: simulate from an assumed truth, analyse with exactly the planned test, repeat at least 1000 times, check false positive rate under the null first, report the Monte Carlo interval.
- Never compute power from the effect you just observed. It adds nothing beyond the p-value. After the fact, report the interval around the effect, or the smallest effect the study could have detected.

If the achievable size cannot detect the effect that matters, say what the study can and cannot show. Do not hide it.

## Claims that need a different design

- "No difference" or "equivalent" needs a stated margin and an equivalence or non-inferiority analysis. A non-significant test does not show equivalence.
- Ranking many methods needs a plan for multiple comparisons.
- Generalisation across settings needs those settings in the data.

## Plan before results, and honest labels

Write the primary comparison, secondary comparisons, exclusions, transformations, handling of missing or failed runs, and stopping rule before looking at outcomes. Timestamp it. When the data were already seen by the analyst (an existing dataset), record exactly what was seen. Anything chosen after that is exploratory and is labelled so. A deviations log lists date, change, reason and likely effect.

## Controls

Add a positive control (should show the effect), a procedural control (should show nothing from the procedure alone) and, when the mechanism allows, a negative control (cannot work through the mechanism but shares the same bias). A control that fails means the setup is suspect, not that the hypothesis is confirmed.

## Reproducibility records

Versions of language, libraries and hardware, random seeds, data version or hash, the exact commands, and where each output file comes from.
