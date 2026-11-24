---
name: research-question
description: Stage 3 of a research project. Use when the user has a topic and a literature review and needs a precise research question. Runs a short Socratic dialogue (question, mechanism, identifiability, validation, risk), classifies the claim, writes falsifiable hypotheses with rival explanations, and ends with a Research Question Card that must pass a readiness gate. Not for searching papers or designing experiments.
---

# Research question

Goal: a question that is specific, answerable with the user's resources, and could be proven wrong.

> Adapted from `research-design-helper` (WenyuChiou/research-hub, MIT), the Research Question Card idea in `research-ideation` (Galaxy-Dawn/claude-scholar, MIT) and the hypothesis workflow in `hypothesis-generation` (K-Dense-AI/scientific-agent-skills, MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## Inputs

Read `01-topic.md`, `02-literature-review.md` and `evidence-ledger.md`. If the review is missing, say so and ask whether to run it first. Pull the gaps with verdict `worth-pursuing` as the starting point.

## Dialogue

Work through five short segments with the user, one at a time. Pre-fill answers from the gap list and the review, and ask the user to confirm or correct. Do not run all five at once.

1. **Question.** Draft three versions, from narrow to broad. For each, say in one sentence what a convincing answer would look like.
2. **Mechanism.** Why would the answer be what you expect? If there is no plausible mechanism, say so, because the work may be purely descriptive.
3. **Identifiability.** Could the planned data and method tell your explanation apart from rival explanations? If not, the question needs changing before any experiment is run.
4. **Validation.** How will you know the result is right: baselines, held-out data, replication, an external check?
5. **Risk.** What is the most likely way this fails, and what is the fallback question?

## Classify the claim

Mark the question as descriptive, associational, predictive, causal or mechanistic. Never let an associational design carry a causal question. If it is causal, state the effect you want to estimate before choosing methods.

## Hypotheses

Write 1 to 3. For each: the prediction, the rival explanation it competes with, and the result that would count against it. Add the null. A hypothesis that cannot fail is not a hypothesis, so rewrite it. Treat all hypotheses as candidates to challenge, not findings, and label them `candidate`. Write your own rivals first, then add more, so the list is not anchored on one idea.

## Test the question

Check each draft: specific (two people read it the same way), answerable (data and time exist), novel (differs from the closest papers, named from the ledger), worth answering (say who benefits). Recommend one and explain why in a few sentences.

## Readiness gate

Before the next stage, the card below must have no empty field. If a field cannot be filled, name the evidence that is missing and stop there.

## Reference files

- `references/question-framing.md`: object definitions, rival explanation classes, claim types, how to derive a prediction
- `references/socratic-segments.md`: the prompts for each of the five segments. Read it before the dialogue.
## Output

Save `research/<project-slug>/03-research-question.md` containing the **Research Question Card**:

- Question (one sentence)
- Claim type
- Mechanism
- Hypotheses, each with prediction, rival, and what would count against it
- Null hypothesis
- Scope: in and out
- Expected contributions (at most 3, modest wording)
- Evidence behind it (ledger IDs)
- Validation plan (one line, detailed in the next stage)
- Main risk and fallback question

## Rules

- Contributions must be ones the method can actually deliver.
- Do not turn an interesting pattern in the literature into a claim of fact.
- Keep scope small enough to finish.
