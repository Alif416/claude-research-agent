# Dead ends and contribution type

Adapted from `gap-to-topic` and its `dead-end-history` and `contribution-typing` references (WenyuChiou/research-hub, MIT). Rewritten and shortened for this project.

## Why check for dead ends

A gap can be open because nobody tried, or because people tried and gave up. A normal search cannot tell the two apart, because failures are rarely published and often sit in Limitations sections. Run a separate pass for it.

## Three passes (run all three)

1. **Failure-term queries.** The gap topic plus words like: limitations, negative result, fails to, open problem, remains unsolved, intractable.
2. **Survey sweep.** Find review papers on the topic and read what they say is unsolved.
3. **Limitations read.** For the closest papers, read their Limitations and Future work sections.

## What counts as a signal

- A paper or survey says the topic itself has failed or is unsolved, as a standing verdict
- A limitations or future-work admission ("we were unable to...", "remains an open challenge")
- Activity that clusters in a few years and then stops, but only when one of the above also appears. Silence alone can mean the problem was solved.

Do not count a sentence like "X fails, therefore we propose Y" as a verdict. That paper is an attempt. Follow its outcome.

## Status per gap

| Status | Meaning |
|---|---|
| `genuinely-open` | No failure evidence and no survey engaged the problem. Still carries the recall caveat. |
| `dead-end-fundamental` | Failure is blamed on the problem itself, and two or more papers or a survey agree |
| `dead-end-stale` | Failure is blamed on a specific old tool or method, and a successor that plausibly removes the blocker is in what you retrieved. This is the opportunity case. |
| `partially-attempted` | Attempts exist, evidence is mixed, or a blocker is named but no successor was found. Needs the user's read. |

A stale label needs both parts: the blocker is a tool, and a real successor is in your results. If you cannot name the successor from the results, use `partially-attempted`. Do not relabel every dead end as stale to be optimistic.

Every quoted failure sentence must be checked against the source. A quote you cannot confirm is dropped, not softened.

## Contribution type

A descriptive lens, not a quality verdict. Incremental work is often valuable.

| Type | Meaning | Test |
|---|---|---|
| problem-solving | Makes something possible that was not, or removes a blocker that earlier work named | Does this open a class of work that was closed? |
| incremental | Better, faster or more accurate on a task that already worked, or an existing method on a new dataset or domain | Is this more or better of something that already worked? |
| borderline | Only when the candidate claims a new capability but a weaker version already exists, or when the opening type is itself unclear, or the statement is too vague to classify | Not a default for "hard to call" |

Counter-check the usual bias. Method-limitation gaps tend to be labelled problem-solving and new-application gaps incremental. Before settling, say whether this candidate breaks that default. For a new-application gap, say why the new domain does or does not amount to a new capability, not just a new setting.

A removed blocker only counts if the blocker was named in the dead-end evidence for the same gap, and the justification cites that same sentence.

## Candidate revision record

After comparing against the closest and contrary work, write down: the original claim, the overlap you actually saw, the revised claim, and the one test that would still tell them apart. Do not leave an unchanged novelty claim in place when prior work already narrows it.

## Decision relevance

For each candidate say who benefits, what changes if it works, and why the closest alternative does not already solve it. A new combination of methods is not a contribution by itself.

## Feasibility, in more detail

Check data access and quality (does the data have the variables and granularity you need, not just a download link), skills and compute, time and cost, ethics and approvals, and a way to validate the result. A missing prerequisite is unknown, not a failure. Name a next check for each unknown. A hard blocker cannot be offset by a good score elsewhere. Describe the smallest study that would still answer the question, with the baseline it needs.
