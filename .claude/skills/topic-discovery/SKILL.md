---
name: topic-discovery
description: Stage 1 of a research project. Use when the user gives a broad research area and wants a specific, publishable topic inside it. Brainstorms, maps the field, finds gaps of five kinds, and runs each candidate through three go/no-go gates (open, contribution, feasibility) before recommending one. Not for in-depth literature review.
---

# Topic discovery

Goal: go from a broad area to a short list of candidate topics that each have a written verdict, then help the user choose one.

> Adapted from the ideas in `research-ideation` (Galaxy-Dawn/claude-scholar, MIT), `gap-to-topic` (WenyuChiou/research-hub, MIT) and `hypothesis-generation` (K-Dense-AI/scientific-agent-skills, MIT). Rewritten and merged for this project. See THIRD-PARTY-NOTICES.md.

## 1. Intake

Ask only what is missing: the area and any preferred sub-area, time available, compute, programming skills, data access, what the work is for (course project, thesis, paper), and anything already tried. Also ask whether the user has an advisor or venue in mind.

## 2. Brainstorm

Use 5W1H (what, why, who, when, where, how) on the area to produce 8 to 12 rough ideas. Keep them rough. Do not filter yet.

## 3. Map the field

Run web searches and the scripts in `../literature-review/scripts/`. Find recent surveys and the most cited papers of the last 3 years. Surveys show structure quickly. Record the search boundary now: databases used, date, years covered, and queries. This boundary goes into the output file.

## 4. Find gaps

Look for five kinds of gap and label each one:
- **Literature gap:** a question nobody has answered
- **Method gap:** a known problem solved only with weak or dated methods
- **Application gap:** a method that works in one setting and has not been tried in another
- **Cross-field gap:** a solution from one field that has not reached another
- **Time gap:** an old result that recent data or tools may overturn

Good sources are "limitations" and "future work" sections of recent papers and the open challenges listed in surveys.

## 5. Write candidate cards

For each of 3 to 5 candidates: title in one line, the gap and its type, why it matters, data and tools needed, effort (low, medium, high), and the 2 or 3 closest existing papers with links you actually saw.

## 6. Run the three gates

Give each candidate a verdict with a reason. Be strict.

1. **Open.** Is the gap still unaddressed? Search the idea in plain words and with synonyms. Never write "nobody has done this". Write "no close match found within this search boundary".
2. **Contribution.** Would closing it add something real, or is it a small permutation of existing work (new dataset name, same method, same result)? Say who would care about the answer.
3. **Feasibility.** Can the user close it with their time, compute, data and skills? Name the main blocker.

Verdicts: `worth-pursuing`, `reshape` (say how), or `do-not-pursue` (say why). Keep rejected candidates in the file so the user sees what was considered.

## 7. Recommend and record the choice

Name the top pick in 3 or 4 honest sentences, including the biggest risk and a fallback if it fails. The user decides. Ask which candidate they choose, or whether they want to reshape one. Then add a **Chosen topic** section at the top of `01-topic.md` with the topic in one line, which candidate it was, the user's reason, and whether it differs from your recommendation. Mark the other candidates `not chosen` and keep them. Update `00-state.md` with the same choice. Do not hand over to the next stage until this is written.

## Reference files

- `references/search-boundary-and-gates.md`: search boundary block, evidence tags, kill and upgrade test, what counts as a small contribution
- `references/dead-ends-and-contribution.md`: how to check that a gap is open and not abandoned, contribution types, feasibility in detail. Read it before step 6.
## Output

Save `research/<project-slug>/01-topic.md` with: intake summary, search boundary, gap list with types, candidate cards, gate table (candidate, open, contribution, feasibility, verdict, reason), recommendation. Add every source you cite to `evidence-ledger.md` (template in the literature-review skill).

## Rules

- Every paper mentioned needs a link seen in a real search result.
- A small topic finished well beats a large one left half done.
- If the user already has a topic, skip to step 3 and run the gates on it. A topic that fails a gate is a finding, not a failure of the stage.
