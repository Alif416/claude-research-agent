---
name: research-question
description: Stage 3 of a research project. Use when the user has a topic and a literature review and needs a precise research question, hypotheses, contributions and scope. Not for searching papers or designing experiments.
---

# Research question

Goal: turn the gaps found in the literature review into a question that is specific, answerable, and worth answering.

## Steps

1. Read `01-topic.md` and `02-literature-review.md` in the project folder. If the review is missing, say so and ask whether to run it first.
2. List the gaps from the review. Pick the one or two that are real, reachable, and matter to the field.
3. Draft 3 versions of the research question, from narrow to broad. For each, write one sentence on what a convincing answer would look like.
4. Test each draft:
   - **Specific:** could two people read it and mean the same thing?
   - **Answerable:** can data or an experiment settle it within the user's time and compute?
   - **Novel:** does it differ from the closest papers in the review? Name them.
   - **Worth it:** who would care about the answer?
5. Recommend one. Explain the choice briefly.
6. For the chosen question write:
   - 1 to 3 hypotheses that could be proven wrong
   - Expected contributions (at most 3, stated without hype)
   - Scope: what is in, and what is explicitly out
   - Main risks and what the user would do if the main idea fails

## Output file

Save to `research/<project-slug>/03-research-question.md`.

## Rules

- A hypothesis that cannot fail is not a hypothesis. Rewrite it.
- Do not promise contributions the method cannot deliver. Be modest.
- Keep scope small enough to finish.
