---
name: paper-writing
description: Stage 6 of a research project. Use when the user wants to draft the research paper, or a specific section such as abstract, introduction, related work, methods, results, discussion or conclusion, from the earlier stage files. Not for running experiments.
---

# Paper writing

Goal: a clear first draft built from the project files, in the user's voice, with no invented content.

## Steps

1. Ask which venue or format applies (course report, thesis chapter, conference, journal) and the page or word limit. If the user has a template, use its section order. Otherwise use: Abstract, Introduction, Related Work, Method, Experiments, Results, Discussion, Limitations, Conclusion, References.
2. Read all earlier stage files. Draft from them. Do not add claims, numbers or citations that are not in those files.
3. Write in this order, which is easier than front to back: Method, Experiments and Results, Related Work, Introduction, Discussion and Limitations, Conclusion, Abstract last.
4. Introduction pattern: the problem and why it matters, what is missing in current work, what this paper does, what it contributes (matching the research question stage), and a short roadmap only if the venue expects one.
5. Related work comes from the literature review, grouped by theme, and ends by saying how this work differs.
6. Every number in the text must match `05-results.md`. Every citation must be in the verified reference list from the literature review.
7. Ask for the user's feedback after each major section before moving on, unless they asked for a full draft in one go.

## Style

- Plain, direct sentences. Say what was done and what was found.
- No em-dashes, no hype words ("novel", "groundbreaking", "state-of-the-art") unless the results clearly support them, and no filler openers.
- Prefer active voice. Define each term once, then use it the same way every time.
- Match the user's own writing if they share samples.

## Output file

Save to `research/<project-slug>/06-draft.md`, one section at a time or whole.

## Rules

- Do not fabricate. If a section lacks material, write a short placeholder note saying what is missing.
- Do not paste long passages from other papers. Paraphrase and cite.
- Flag claims that are stronger than the evidence.
