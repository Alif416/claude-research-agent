---
name: analysis-and-results
description: Stage 5 of a research project. Use when the user wants to run the planned experiments or analysis, write the code, and report results with tables, figures and honest interpretation. Not for planning the method or writing the paper.
---

# Analysis and results

Goal: results that are correct, reproducible, and reported honestly, including the parts that did not work.

## Steps

1. Read `04-methodology.md`. Confirm with the user which part to run now. Start with the smallest experiment that can show whether the idea has any signal.
2. Set up the work in `research/<project-slug>/code/`: a README with how to run, a requirements file, fixed random seeds, and one script per experiment.
3. Write the code, run it, and read the actual output. If it errors, fix it. If it runs but looks wrong (perfect scores, identical numbers across runs, loss that never moves), treat it as a bug and investigate before reporting anything.
4. Save raw outputs (CSV or JSON) in `results/`. Make tables and figures from those files only, never from numbers typed by hand.
5. Run each stochastic experiment with several seeds and report mean and spread. Use the statistical test named in the methodology when comparing against baselines.
6. Interpret. For each hypothesis say supported, not supported, or inconclusive, and point to the evidence. Include negative results and anything surprising.
7. Note limits: what the results do not show, and what you would check next.

## Output file

Save to `research/<project-slug>/05-results.md` with: what was run, setup and seeds, results tables, figures, interpretation per hypothesis, limitations, and how to reproduce.

## Rules

- Never make up, round up, or adjust a result. If a run failed or was skipped, say so.
- Never tune on the test set. If the user asks for this, explain why it would invalidate the result.
- Report what was actually run, even if it differs from the plan, and say why.
- If compute is not available in this environment, write the code and the run instructions, and say clearly that nothing was executed.
