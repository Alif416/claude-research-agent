# Statistics guide

Adapted from `statistical-analysis` (K-Dense-AI/scientific-agent-skills, MIT) and `results-analysis` (Galaxy-Dawn/claude-scholar, MIT).

## Workflow

1. Frame first: hypothesis, outcome, predictor, design (independent or paired, number of groups), unit, dependence, multiplicity family. Do this before looking at outcomes.
2. Look at the data: per group n, mean, spread, median, missing values. Plot raw data before testing. Unequal groups, missing data, floor or ceiling effects and outliers change the test, so tell the user.
3. Pick the test from the table below.
4. Check assumptions with plots and the design in mind. A non-significant normality or variance test does not prove the assumption holds. Do not switch tests automatically at a p-value cutoff.
5. Run the test and report an effect size and its interval beside it.
6. Report descriptives, exact statistics, effect size with interval, and which checks were done.

## Picking a test

| Situation | Usual choice |
|---|---|
| Two independent groups, continuous | Welch t-test (do not assume equal variance) |
| Two paired measurements | Paired t-test on the differences |
| Three or more independent groups | Welch ANOVA, or ANOVA if equal variance is justified; pairwise follow-up with a correction |
| Rank-based question | Mann-Whitney, Wilcoxon signed-rank, Kruskal-Wallis, Friedman. These test distribution or rank shifts, not medians in general |
| Two continuous variables | Pearson for linear, Spearman for monotone |
| Binary or count outcome | Logistic or Poisson style regression, chi-square or exact test for tables |
| Repeated or clustered data | A model that represents the dependence (mixed model, clustered errors) |
| Several methods across several datasets | Paired comparison per dataset, then a rank-based test across datasets with a post-hoc correction |
| Time to event | Survival methods, not a plain mean comparison |

## Effect sizes

- Mean difference: raw difference with interval, plus standardised (Cohen d or Hedges g) when scales differ. State the sign.
- Rank tests: probability of superiority or Cliff delta.
- ANOVA: partial eta squared or omega squared.
- Correlation: r with interval.
- Tables: odds ratio or risk difference, with the baseline risk. A relative effect without the baseline misleads.

## Intervals

Use a 95% interval unless there is a reason otherwise, and say how it was computed. For machine learning results with few seeds, use a bootstrap or a t interval over seeds and say how many seeds. Report all runs, not the best.

## Claims about no effect

A non-significant test does not show there is no effect or that two methods are equal. Check whether the interval rules out differences that matter. For an equivalence or non-inferiority claim, the margin must have been fixed in the plan and the matching analysis run. Otherwise say "no clear difference was found, and the interval allows differences up to X".

## Multiple comparisons

Count every comparison made, including ones you looked at and dropped. Use a family-wise correction (Holm is a good default) or false discovery rate control, and say which.

## Things to refuse or flag

- picking the best seed or checkpoint on the test set
- observed or post-hoc power
- p-values with no effect size
- treating rows from one subject or one seed as independent
- an interpretation that contradicts the file's own test or unit

## Audit mode checklist

When there are no new runs, check what exists and report:
- which statistics are valid with the data given
- what is missing (seeds, raw per-run values, unit, baselines, protocol)
- the strongest claim the evidence could support
- what would be needed to support something stronger

## Claim candidate entry

```
Claim:
Evidence: (file, table, number, ledger ID)
Allowed wording:
Forbidden stronger wording:
Uncertainty:
Next check:
Decision: keep / weaken / revise / discard
```

Example. Evidence: method A beats baseline B by 1.2 points over 5 seeds, interval 0.1 to 2.3. Allowed: "A scored higher than B on this benchmark in our runs". Forbidden: "A is better than B in general", "A significantly outperforms B" if no test supports the word.

## Figures

A figure earns its place if it answers: why does it exist, what should the reader notice, what does it change in belief or next steps. Plot from the saved result files, show uncertainty, label axes and units, state n, and use shapes or line styles as well as colour. Save the script that draws it.
