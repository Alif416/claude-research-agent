<h1 align="center">Claude Research Agent</h1>

<p align="center"><b>An end-to-end research assistant for Claude Code.</b><br>
From a broad idea to a reviewed paper draft, one verified stage at a time.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://docs.claude.com/en/docs/claude-code/overview"><img alt="Built for Claude Code" src="https://img.shields.io/badge/built%20for-Claude%20Code-orange.svg"></a>
  <a href="https://github.com/Alif416/claude-research-agent/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Alif416/claude-research-agent"></a>
  <a href="https://github.com/Alif416/claude-research-agent/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Alif416/claude-research-agent?style=social"></a>
</p>

<p align="center">
  <a href="#installation">Install</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#the-seven-stages">The seven stages</a> ·
  <a href="#how-the-literature-search-works">Literature search</a> ·
  <a href="#credits">Credits</a> ·
  <a href="https://github.com/Alif416/claude-research-agent/issues">Report an issue</a>
</p>

---

Claude Research Agent is a Claude Code agent that guides a research project from a blank page to a finished paper, one stage at a time.

You give it a research area. It helps you find a topic, review the literature, shape a research question, plan the method, run the analysis, draft the paper, and check the draft before you submit. Each stage has its own skill, so the agent follows a focused playbook for the job at hand instead of improvising everything from one big prompt. Every paper and number goes into a shared evidence ledger, and the draft may only state what traces back to it.

---

## Table of contents

1. [The problem](#the-problem)
2. [What this project is](#what-this-project-is)
3. [How it works](#how-it-works)
4. [The seven stages](#the-seven-stages)
5. [Requirements](#requirements)
6. [Installation](#installation)
7. [Quick start](#quick-start)
8. [A full walkthrough](#a-full-walkthrough)
9. [Project folder layout](#project-folder-layout)
10. [How the literature search works](#how-the-literature-search-works)
11. [Output formats](#output-formats)
12. [Built-in rules](#built-in-rules)
13. [Customizing the skills](#customizing-the-skills)
14. [Limitations](#limitations)
15. [Troubleshooting](#troubleshooting)
16. [Repository structure](#repository-structure)
17. [Credits](#credits)
18. [Contributing](#contributing)
19. [License](#license)

---

## The problem

Doing research well takes a long chain of different jobs, and each one needs a different way of thinking.

- Picking a topic means scanning a whole field and spotting a gap that is real, reachable, and not already solved.
- A literature review means searching several databases, screening dozens of papers, and writing a synthesis rather than a pile of summaries.
- A research question has to be specific and testable, not a vague wish.
- A methodology has to be something you can actually run with your time and compute.
- Writing and review mean keeping every claim, number, and citation consistent.

Students and early researchers often do this alone, with little guidance, and with a few common failure modes:

- **Topics that are too broad or already done.** Weeks go into an idea that a quick search would have shown was taken.
- **Shallow or one-sided reviews.** Papers are listed one after another with no themes, no comparison, and no clear gap.
- **Invented or wrong citations.** General-purpose AI tools sometimes produce references that look real but do not exist. One fake citation can damage a paper.
- **Plans that outgrow the resources.** A method that needs a cluster is proposed to someone with a laptop.
- **Inconsistent write-ups.** Numbers in the abstract do not match the results table, and terms change from section to section.

## What this project is

`claude-research-agent` is a set of Claude Code configuration files: one agent definition and seven skills. There is no server and no app to run. You copy the files into a project, and Claude Code gains a research assistant that:

- works through the project in a fixed order of stages,
- uses only the skill that belongs to the current stage,
- saves each stage's result as a file in your project so the work is traceable,
- searches arXiv and Semantic Scholar through small included scripts, plus web search,
- refuses to invent papers, numbers, or results, and marks anything it could not verify,
- asks you which output format you want before it finishes each stage.

It is meant to be a careful collaborator. You still make the decisions: which topic to pick, which question to ask, whether a result is convincing.

## How it works

There are two kinds of files.

**The agent** (`.claude/agents/research-agent.md`) is the coordinator. It knows the order of the stages, keeps a state file for each project, applies the rules that hold across every stage (no fabrication, plain writing, ask before assuming), and decides which skill to use.

**The skills** (`.claude/skills/<name>/SKILL.md`) are the playbooks. Each one covers exactly one stage: what to ask you first, the steps to follow, what file to produce, and the rules for that stage. A skill's short description tells Claude when to use it, so asking for "a literature review" brings in the literature review skill and nothing else.

```
You: "Do the literature review on <topic>"
        |
        v
  research-agent  --- reads research/<project>/00-state.md
        |
        v
  literature-review skill  --- searches, screens, reads, synthesises
        |
        v
  research/<project>/02-literature-review.md
        |
        v
  asks you: Markdown, Word, PDF, or chat reply?
```

You can run the stages in order from start to finish, or jump to one stage if you already have the earlier work. If you ask for a stage whose earlier input is missing, the agent tells you and asks whether to run the earlier stage first.

## The seven stages

| # | Stage | Skill | What it does | Saved as |
|---|---|---|---|---|
| 1 | Find a topic | `topic-discovery` | Maps a broad area, finds gaps, proposes 3 to 5 candidate topics, checks each for novelty and for fit with your time, compute, and skills, and recommends one | `01-topic.md` |
| 2 | Literature review | `literature-review` | Runs many searches, removes duplicates, screens papers, reads the best ones, groups them into themes, builds a comparison table, lists gaps, and verifies every citation | `02-literature-review.md` |
| 3 | Research question | `research-question` | Turns the gaps into a precise question, tests several drafts, writes falsifiable hypotheses, states scope and expected contributions, and lists risks | `03-research-question.md` |
| 4 | Methodology | `methodology-design` | Chooses datasets, method, baselines, metrics, ablations, and validity checks, and writes a work plan sized to your resources | `04-methodology.md` |
| 5 | Analysis and results | `analysis-and-results` | Writes and runs code for the planned experiments, uses fixed seeds, reports spread across runs, and interprets each hypothesis as supported, not supported, or inconclusive | `05-results.md` plus `code/` and `results/` |
| 6 | Paper draft | `paper-writing` | Drafts the paper from the earlier files, section by section, in plain language, with numbers and citations taken only from those files | `06-draft.md` |
| 7 | Final review | `final-review` | Checks claims against evidence, numbers against raw results, citations against searches, then simulates a tough reviewer and lists fixes by priority | `07-review.md` |

## Requirements

- [Claude Code](https://docs.claude.com/en/docs/claude-code/overview), installed and signed in
- Python 3.8 or newer for the two search scripts (standard library only, nothing to `pip install`)
- Internet access, for paper search and web lookups
- Optional: a free [Semantic Scholar API key](https://www.semanticscholar.org/product/api) to avoid rate limits

## Installation

You can install it for a single project, or for every project on your machine.

**Option 1: one project**

```bash
git clone https://github.com/Alif416/claude-research-agent.git
cp -r claude-research-agent/.claude /path/to/your/research-project/
```

**Option 2: every project**

```bash
git clone https://github.com/Alif416/claude-research-agent.git
cp -r claude-research-agent/.claude/agents/. ~/.claude/agents/
cp -r claude-research-agent/.claude/skills/. ~/.claude/skills/
```

Then restart Claude Code and type `/agents`. You should see `research-agent` in the list.

If you use the Semantic Scholar key:

```bash
export S2_API_KEY="your-key-here"
```

## Quick start

Open Claude Code in your project folder and ask:

```
Use the research-agent to find a research topic in <your area>
```

Then continue stage by stage:

```
Use the research-agent to do the literature review on <chosen topic>
Use the research-agent to write the research question
Use the research-agent to design the methodology
Use the research-agent to run the experiments
Use the research-agent to draft the paper
Use the research-agent to review the draft
```

At any point you can say:

```
Use the research-agent to continue the project
```

and it will read the state file and pick up where you stopped.

Some Claude Code versions can run the whole session as the agent:

```bash
claude --agent research-agent
```

This lets the agent ask you questions directly. Check `claude --help` to see whether your version supports it.

## A full walkthrough

This is what a typical run looks like. The example area is "federated learning in healthcare".

**1. Topic discovery.** You ask for a topic. The agent first asks about your limits: time, compute, programming skills, and what the work is for (course project, thesis, paper). It then searches for recent surveys and highly cited papers, reads their open challenges, and drafts several candidate topics. For each one it searches for the idea in plain words and records the closest existing papers. It recommends one and explains the risks. You choose.

**2. Literature review.** The agent confirms scope: year range, how many papers, and the style of review. It writes several search queries, runs each through arXiv and Semantic Scholar, and logs them. It removes duplicates, screens by relevance, and reads the strongest papers in more detail, noting when it only saw an abstract. It groups the papers into themes, writes the synthesis, builds a comparison table, and lists the gaps. A last pass checks every reference against the search log.

**3. Research question.** It reads the gaps, proposes three versions of the question from narrow to broad, and tests each for specificity, answerability, novelty, and value. It recommends one and writes hypotheses that could actually be proven wrong.

**4. Methodology.** It picks datasets and confirms they exist, chooses the method and baselines, defines metrics and the statistical comparison, plans ablations, lists threats to validity, and ends with an ordered work plan whose first item is the smallest experiment that could show whether the idea has any signal.

**5. Analysis and results.** It sets up a `code/` folder, writes the scripts, runs them, and reads the real output. If results look wrong (for example, perfect scores), it treats that as a bug. It runs multiple seeds, reports mean and spread, and interprets each hypothesis honestly, including negative results.

**6. Paper draft.** It asks for the venue and length limit, then drafts from the project files, usually starting with the method and results and writing the abstract last.

**7. Final review.** It checks every claim and number, verifies the citations again, looks for inconsistencies, imagines the five hardest reviewer questions, and gives you a prioritized fix list. It does not change the paper unless you ask.

After each stage the agent gives a short summary, asks which output format you want, and asks whether to continue.

## Project folder layout

Each research project gets its own folder under `research/` in the directory where you run Claude Code:

```
research/
  federated-learning-healthcare/
    00-state.md                 current stage, decisions made, next step
    evidence-ledger.md          sources, claims and numbers shared by all stages
    01-topic.md
    02-literature-review.md
    03-research-question.md
    04-methodology.md
    05-results.md
    06-draft.md
    07-review.md
    code/                       scripts, README, requirements, seeds
    results/                    raw CSV or JSON output behind every table
```

`00-state.md` is what lets you stop and return days later. The agent reads it first and knows what has been decided.

## How the literature search works

The literature review skill includes two scripts in `.claude/skills/literature-review/scripts/`. They use only the Python standard library.

```bash
python3 search_arxiv.py "federated learning remote patient monitoring" --max 15
python3 search_arxiv.py "federated learning" --max 10 --sort date

python3 search_semantic_scholar.py "federated learning remote patient monitoring" --max 15 --year 2021-
```

Each script prints one JSON object per line.

- **arXiv** returns title, authors, year, abstract, link, and PDF link. It is strongest for computer science, machine learning, physics, and mathematics.
- **Semantic Scholar** returns the same, plus venue, citation count, DOI, and an open-access PDF link when one exists. It covers most fields.

The agent also uses web search for what these two sources miss: journal articles, theses, dataset pages, and benchmark leaderboards.

Every search is logged in the review file so you can repeat it later.

## Output formats

At the end of each stage the agent asks which format you want:

- Markdown file
- Word document (`.docx`)
- PDF
- A reply in the chat only

It does not choose for you. The stage's result is always saved as Markdown in the project folder first, and the other formats are produced from it.

## Built-in rules

These apply in every stage.

- **No invented sources.** A paper, author, number, quote, dataset, or result may only appear if it came from a search or a file the agent actually saw in the session. Anything it could not confirm is marked `[unverified]`, with the reason.
- **Honest failure.** If a search returns nothing or a tool fails, the agent says so. It does not fill the gap from memory.
- **Abstract-only is disclosed.** If it only read an abstract, the notes say so.
- **No test-set tuning.** If asked to tune on the test set, the agent explains why that would invalidate the result.
- **Results stay real.** A number is never rounded up, adjusted, or typed by hand into a table. Tables come from the raw result files.
- **Ask when unsure.** Scope, field, and depth are confirmed before the agent spends a lot of effort.
- **One evidence ledger.** A single `evidence-ledger.md` tracks every source, claim and number across all stages. The paper can only state what traces back to a row in it.
- **Stage gates.** Each stage must produce what the next one needs (for example a Research Question Card with no empty field) before the agent moves on.
- **Plain writing.** Short, direct sentences, no filler, no hype words, no em-dashes.

## Customizing the skills

The skills are plain Markdown, so you can edit them to fit your needs. Most of the quality of the agent comes from how well the skills match your field and your standards.

Common changes:

- **Your field.** Add field-specific sources to `literature-review` (PubMed for medicine, SSRN for economics, ACL Anthology for NLP).
- **Your venue.** Put your conference or journal template and page limit into `paper-writing`.
- **Your rules.** Add your department's requirements for ethics, data handling, or citation style.
- **A stage you do not need.** Remove the skill folder and take its name out of the `skills:` line and the stage list in `research-agent.md`.
- **A new stage.** Add a folder with a `SKILL.md` that has a `name`, a specific `description`, and the steps. Then list it in the agent file.

A skill's `description` line decides when it triggers, so keep it specific to one stage.

## Limitations

Please read these before relying on the output.

- **It does not replace the researcher.** It helps with searching, structuring, drafting, and checking. The judgment about what is worth studying and whether a result is convincing is yours.
- **Verify the references yourself before submitting.** The agent only cites papers it found in searches, and a final stage checks them again, but you should open the key papers and confirm they say what the review claims.
- **Paywalled papers.** It can read abstracts and open-access PDFs. It cannot read articles behind a paywall, and it says when it only saw an abstract.
- **Search coverage.** arXiv and Semantic Scholar do not cover everything. Work in fields with other major databases may need those added.
- **Rate limits.** Semantic Scholar limits anonymous use. Heavy searching may need an API key.
- **Compute.** The analysis stage runs code on the machine where Claude Code runs. Large training jobs need suitable hardware, and the agent will say when it wrote code but did not run it.
- **Subagent questions.** Depending on your Claude Code version, a subagent may not be able to ask you questions directly. In that case it ends its message with the question and the main session passes it to you.
- **Early version.** The skills have been written carefully but have not been tested across many fields. Expect to tune them against your own projects.

## Troubleshooting

**`research-agent` does not appear in `/agents`.**
Check that the file is at `.claude/agents/research-agent.md` in your project root, or `~/.claude/agents/` for a global install. Restart Claude Code after copying.

**A skill does not trigger.**
Skills trigger from their description. Ask for the stage by name, for example "run the literature-review skill", or make the description in the skill's `SKILL.md` more specific.

**The Semantic Scholar script prints an HTTP 429 error.**
You hit the rate limit. Wait a minute and try again, or set `S2_API_KEY`.

**A search script prints a network error.**
Check your connection, and check whether a proxy or firewall blocks `export.arxiv.org` or `api.semanticscholar.org`.

**The agent skipped asking about the output format.**
Remind it: "Ask me which output format I want for this stage." You can also strengthen the "Ending every stage" section of `research-agent.md`.

**The agent says an earlier stage is missing.**
It looks for `research/<project>/0X-*.md`. Either run the earlier stage, or tell it to continue without it.

## Repository structure

```
claude-research-agent/
  README.md
  LICENSE
  THIRD-PARTY-NOTICES.md
  .claude/
    agents/
      research-agent.md
    skills/
      topic-discovery/
        SKILL.md
        references/
          search-boundary-and-gates.md
          dead-ends-and-contribution.md
      literature-review/
        SKILL.md
        references/
          search-strategies.md
        scripts/
          search_arxiv.py
          search_semantic_scholar.py
          verify_citation.py
        templates/
          evidence-ledger.md
      research-question/
        SKILL.md
        references/
          question-framing.md
          socratic-segments.md
      methodology-design/
        SKILL.md
        references/
          design-and-power.md
        templates/
          analysis-plan.md
      analysis-and-results/
        SKILL.md
        references/
          statistics-guide.md
      paper-writing/
        SKILL.md
        scripts/
          lint_style.py
        references/
          structure-and-reporting.md
          ai-patterns.md
      final-review/
        SKILL.md
        references/
          review-checklist.md
```

## Credits

The seven skills were adapted from the methods of several open source projects, rewritten in our own words and merged into one connected workflow. Thank you to their authors.

| Stage | Adapted from | License |
|---|---|---|
| 1. Topic discovery | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) (`research-ideation`), [WenyuChiou/research-hub](https://github.com/WenyuChiou/research-hub) (`gap-to-topic`), [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (`hypothesis-generation`) | MIT |
| 2. Literature review | K-Dense `literature-review`, WenyuChiou `literature-triage-matrix`, claude-scholar `literature-reviewer` | MIT |
| 3. Research question | WenyuChiou `research-design-helper`, claude-scholar `research-ideation`, K-Dense `hypothesis-generation` | MIT |
| 4. Methodology | K-Dense `experimental-design` and `statistical-power`, [fcakyon/phd-skills](https://github.com/fcakyon/phd-skills) `experiment-design` | MIT |
| 5. Analysis and results | claude-scholar `results-analysis`, K-Dense `statistical-analysis` | MIT |
| 6. Paper writing | K-Dense `scientific-writing`, claude-scholar `writing-anti-ai` | MIT |
| 7. Final review | claude-scholar `paper-self-review` and `citation-verification`, K-Dense `peer-review`, phd-skills `paper-check` | MIT |

What is new here: one shared evidence ledger across all stages, hard gates between stages, a citation verification script with fixed matching rules, and the single agent that ties the stages together. Full details and the notices to keep are in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

If these skills materially help your work, the K-Dense authors ask that you cite the Scientific Agent Skills library (Kassis et al., 2026, arXiv:2609.00065). Check the current arXiv record for details before citing.

## Contributing

Contributions are welcome. Good places to start:

- field-specific versions of the skills (medicine, social science, economics, and so on)
- more search sources for the literature review (PubMed, ACL Anthology, OpenAlex)
- better checks in `final-review`
- examples of a completed project folder
- bug reports from real use, with the stage and prompt that caused the problem

To contribute, open an issue to discuss the change, then send a pull request. Please keep the plain-language style used across the skills.

## License

Released under the [MIT License](LICENSE). You are free to use, copy, modify, and share it, as long as the copyright notice stays.
