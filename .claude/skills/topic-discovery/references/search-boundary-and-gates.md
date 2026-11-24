# Search boundary and gate notes

Adapted from the dated evidence boundary in `hypothesis-generation` (K-Dense-AI/scientific-agent-skills, MIT) and the three-gate decision memo in `gap-to-topic` (WenyuChiou, MIT).

## Search boundary record

Put this block at the top of `01-topic.md`. A search can only show what was searched. It never shows that nothing exists.

```
Search date:
Sources searched: (web, arXiv, Semantic Scholar, others)
Years covered:
Queries run (exact strings):
Filters used (language, venue, field):
Included source types: (papers, surveys, preprints, reports)
Excluded source types:
Known limits: (paywalls, non-English work, one database only, failed requests)
```

Wording rules:
- Write "no close match found within this search boundary". Never write "no prior work exists" or "this is novel".
- A timeout, a rate limit or an empty page is an unknown, not a zero result. Retry or log it as a limit.
- Keep results that argue against the idea. If the search found a paper that already answers the gap, say so plainly.

## Evidence strength tags for gate verdicts

Tag each reason in the gate table:
- `seen`: you opened the source and read the relevant part
- `snippet`: you only saw an abstract or search snippet
- `inferred`: your own reasoning, no source

A verdict that rests on `snippet` or `inferred` only should say so, and the user should treat it as a lead to check.

## Kill and upgrade test

For every `worth-pursuing` or `reshape` candidate write two lines:
- **Kill test:** the one finding that would make you drop it (for example, a 2025 paper that already runs this comparison)
- **Upgrade test:** the one finding that would make it clearly worth the time (for example, a public dataset that fits the setup)

Then run those two checks before the user commits.

## Contribution gate: what counts as small

Be strict. These usually fail the gate:
- same method on a new dataset with no reason to expect a different result
- a different hyperparameter or backbone swap
- combining two known techniques with no argument for why they should interact
- a benchmark that only restates an existing one

These can pass:
- a setting where the standard assumption is known to break
- a measured comparison that settles a disagreement between papers
- a cheaper or simpler method that reaches the same accuracy, with evidence
- a first systematic evaluation of something people already use

## Feasibility gate

Check four things, each as yes, partly or no: time, compute, data access, skills. Name the single largest blocker. If the blocker is data, check that the data exists and the licence allows use before recommending.

## Hypotheses are candidates

When a candidate includes a guessed mechanism, label it `candidate`. It is something to test later, not something the literature has shown.
