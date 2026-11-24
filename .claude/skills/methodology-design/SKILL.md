---
name: methodology-design
description: Stage 4 of a research project. Use when the user has a research question and needs a concrete plan: datasets, methods, baselines, metrics, experimental setup, ablations and validity threats. Not for running the experiments.
---

# Methodology design

Goal: a plan another person could follow and reproduce, sized to the user's real resources.

## Steps

1. Read `03-research-question.md` and the comparison table in `02-literature-review.md`.
2. Ask the user for their limits if not already known: compute (GPU or CPU only), time, programming language, data they already have.
3. Choose the **data**. For each dataset give the name, source link, size, licence, and known problems. Search for it if you are not sure it exists. If the user needs to collect data, outline how, and raise ethics or consent needs.
4. Choose the **method**. Describe the approach in plain steps. Say why it fits the question. Name the closest existing method it builds on, with its citation from the review.
5. Choose **baselines**: at least one simple baseline and one strong published method from the review.
6. Choose **metrics** and say why each one answers the research question. Include how results will be compared (cross-validation, held-out test, number of seeds, statistical test).
7. Plan **ablations or extra checks** that test each hypothesis directly.
8. List **threats to validity**: data leakage, small samples, unfair baselines, metric limits, anything that could make the result misleading. Say how each is handled.
9. Make a **work plan**: ordered tasks, rough time per task, and the first small experiment that tests whether the idea has any signal.

## Output file

Save to `research/<project-slug>/04-methodology.md`.

## Rules

- Only cite datasets and tools you confirmed exist.
- Do not design anything the user cannot run with their resources. Offer a smaller version instead.
- Define everything that affects results (splits, seeds, hyperparameter ranges) so the work can be repeated.
