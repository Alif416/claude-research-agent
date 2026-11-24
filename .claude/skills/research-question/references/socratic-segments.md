# The five segments, with prompts

Adapted from `research-design-helper` (WenyuChiou/research-hub, MIT). Rewritten for this project.

Run in order, one at a time. Save the user's own words. If they cannot answer yet, write `_TODO: reason_` and move on. Never invent an answer for them. Adapt to the work: theory, qualitative and descriptive work do not need a hypothesis, causal mechanism or predictive model. Mark a field `not-applicable` with a reason only when it truly does not apply. An unanswered field is `_TODO_`, not not-applicable.

## 1. Question

- What are you studying, in one sentence?
- Is the target a future observation, a difference now, a mechanism, a description, or something else? What population, setting and time period does the answer cover?
- If a hypothesis is part of the design, what would you see if it were false? Otherwise, what evidence or argument would make you revise the answer?
- For a prediction or decision, what is known at decision time and what only appears later? If time ordering does not matter, say why.
- What is the smallest version you could still answer with the resources you have confirmed? What must it keep (needed data, essential comparisons)? What would it not show?

The user chooses any narrowing of countries, periods, populations or aims. Do not set a fixed duration, do not treat a working prototype as proof of feasibility, do not drop an essential comparison, and do not treat unknown costs as zero.

## 2. Mechanism

- If the claim is causal: A leads to B because of C, then B affects D through E. Otherwise, what reasoning supports the answer?
- Where are you least sure?
- If it is wrong, which step is most likely the broken one?

## 3. Identifiability

- What experiment, dataset, counterfactual, proof or evidence would tell your answer apart from its main alternative?
- Which confounders or rival explanations must you handle?
- If current materials cannot separate them, what minimum extra evidence is needed, and can you get it?
- With only two time points, you can describe change between them. You cannot recover the path between or beyond them.
- A scenario or vignette study shows judgments about that scenario. It does not show real behaviour or outcomes.

## 4. Validation

- Which metric or assessment would support the claim?
- Which baseline or comparison tests it? If none applies, why?
- For a capability comparison: do the method and the baseline get the same variables, the same information at the same time, the same splits and the same resources? Fix any gap before crediting a capability. If the question is about the value of extra information, say what the extra information is and what it costs.
- What smallest gain or reduction in uncertainty would change knowledge or a decision? Use a justified number or a plain criterion. If undecided, leave `_TODO_`. Do not make up a percentage or demand statistical significance as a threshold.
- Where it applies, what setup should not show the gain (a negative control), and what rival does it test?

## 5. Risk

List three to five things that would sink the design:
- the materials or their availability
- the model assumptions or the argument
- how the result is interpreted
- the most likely reason a reviewer would reject it

For each risk: what would the early warning look like, and what would you do?

Carry forward any open items from earlier stages (unknown data access, stale sources) into this list as stated, with their next checks. A well-formed card is not approval that the study will work.
