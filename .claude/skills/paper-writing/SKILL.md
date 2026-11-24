---
name: paper-writing
description: Stage 6 of a research project. Use when the user wants to draft the paper, or a section of it, from the earlier stage files. Writes only from the evidence ledger, keeps unsupported content in an unresolved list, reconciles methods and results, and removes AI-sounding patterns. Not for running experiments.
---

# Paper writing

Goal: a clear first draft in the user's voice, where every fact traces back to the evidence ledger.

> Adapted from `scientific-writing` (K-Dense-AI/scientific-agent-skills, MIT) and `writing-anti-ai` (Galaxy-Dawn/claude-scholar, MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## Intake

Ask what is missing: target venue and its current author instructions (check the official page, do not assume), page or word limit, template, reporting guideline for the study type, and authorship and AI-use disclosure requirements. If the user shares past writing, match it.

## Principles

- Three jobs stay separate: drafting, checking evidence, and approving for submission. You do the first, help with the second, and the user does the third.
- Fluent text is not evidence. Every factual or numeric claim must link to a ledger ID.
- The user is the author and is accountable for the paper. AI is not an author.

## Steps

1. **Set up.** Read all earlier files and `evidence-ledger.md`. List what is missing for each section before writing.
2. **Outline from evidence only.** Each section outline cites ledger IDs. While drafting, tag factual sentences with their IDs, for example `[C007: S003, S011]`, and strip the tags only at the end. Content with no support goes in the `Unresolved` list in the ledger, not into the draft.
3. **Draft in this order:** Method, Experiments and Results, Related Work, Introduction, Discussion and Limitations, Conclusion, Abstract last. Use the venue's section order if it differs.
   - Introduction: the problem and why it matters, what current work misses, what this paper does, contributions that match the research question card.
   - Related work: from the literature review, grouped by theme, ending with how this work differs.
   - Results: only numbers from `05-results.md`, with the same wording limits as the claim candidates. Report null and negative results. Mark exploratory analyses as exploratory.
   - Limitations: honest and specific.
4. **Reconcile.** Check that methods and results describe the same data, splits and metrics. Name any difference in analysis sets.
5. **Cleanup pass for AI patterns.** Cut filler openers and emphasis words, shorten wordy phrases ("in order to" becomes "to"), use "is" instead of "serves as", avoid forced lists of three, drop vague attributions ("experts say"), and vary sentence length. Do not strip meaning, and keep the author's own voice. Score the draft from 1 to 10 on directness, rhythm, trust in the reader, authenticity and density, and fix the lowest.
6. **Show the user** each major section and take feedback before the next, unless they asked for a full draft in one go.

## Reference files

- `references/structure-and-reporting.md`: evidence binding, never-invent list, reporting guidelines by study type, section purposes, consistency checks
- `references/ai-patterns.md`: the pattern list, filler to cut, hedging, voice, and the 1 to 10 score
## Style

Short, direct sentences. Active voice. Define each term once and use it the same way after. No em-dashes, no hype words such as "novel" or "state-of-the-art" unless the results clearly support them.

## Output

Save `research/<project-slug>/06-draft.md`, a section at a time or whole. Update `evidence-ledger.md` with any new IDs.

## Rules

- Never invent a citation, number, method, approval, funding source or disclosure. If missing, write `[MISSING: what is needed]`.
- Never overstate. Keep the uncertainty the results carry.
- Do not turn association into causation.
- Do not paste long passages from other papers. Paraphrase and cite.
- Do not send the unpublished draft to outside services you were not asked to use.
