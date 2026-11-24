# Question framing notes

Adapted from `hypothesis-generation` (K-Dense-AI/scientific-agent-skills, MIT) and `research-design-helper` (WenyuChiou, MIT).

## Keep these objects separate

| Object | What it is |
|---|---|
| Observation | What was measured or reported, with its source and uncertainty |
| Research question | The answerable question that sets scope |
| Hypothesis | A candidate explanation or relationship |
| Mechanism | The process that links conditions to an outcome |
| Prediction | Something observable you derive before looking at the target result |
| Rival explanation | Another account that would give the same pattern, including bias or chance |
| Null hypothesis | The no-effect model a test is run against |
| Evidence | Observations or sources that bear on a claim, never the claim itself |

A mechanism story is not a prediction. A prediction is not evidence. Rejecting one null does not prove a mechanism. Support for one candidate does not remove rivals you did not think of.

## Picking a frame

Use a frame only when it fits.
- Intervention or effect: population, intervention, comparator, outcome, time (PICOT)
- Exposure: population, exposure, comparator, outcome (PECO)
- ML or systems work: task, data, method, comparator, metric, setting
- Qualitative or theory work: construct, context, outcome

Also say what answer would change a decision or add knowledge. "Feasible, Interesting, Novel, Ethical, Relevant" is a prompt for discussion, not a score. Treat "Novel" as open until the search boundary supports it.

## Rival explanation classes

Generate rivals before choosing tests. Try one from each class that plausibly applies:
- the proposed mechanism
- a measurement or preprocessing artefact
- a confounder or common cause
- selection (who or what entered the data)
- reverse direction
- context or boundary conditions (works here, not there)
- chance
- a different mechanism at another scale

Write your own first list before asking a model to expand it. Model-expanded lists tend to look alike and anchor on the first idea.

## Claim types

Decide the claim type before the method.
- Descriptive: what is the pattern
- Associational: do these move together
- Predictive: can X forecast Y
- Causal: does changing X change Y
- Mechanistic: why

A causal question needs its target stated first: population, the change you apply, the comparison, the outcome, the time horizon, and the assumptions that would make a non-experimental estimate valid. If those cannot be stated, reword the question as associational.

## Deriving a prediction

For each hypothesis write:
1. Conditions and boundary conditions
2. The observable and how it is measured
3. The expected pattern
4. A result that would be incompatible with the hypothesis
5. How the result would differ under at least one rival
6. What an unclear result would mean

Prefer tests where the rivals predict clearly different outcomes. If a control is added, it must be something the mechanism cannot act on while sharing the same bias paths. An untreated group alone is not a control.

## Identifiability questions to ask the user

- If your explanation is wrong, what would the data look like?
- Which rival gives the same numbers and how would you tell it apart?
- What would you see in a version of the setup where the mechanism is switched off?

## Readiness check wording

Do not call the question ready if the card has an empty field. A field that cannot be filled becomes a named gap in evidence, and the stage stops until it is closed or the question changes.
