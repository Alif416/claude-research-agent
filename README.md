# claude-research-agent

One Claude Code agent with seven skills that takes a research project from a blank page to a finished paper. You tell it which stage you are on, and it only uses the skill for that stage.

It works on one stage at a time, saves each stage to a file, and asks you which output format you want (Markdown, Word, PDF, or a chat reply) before it finishes.

| Stage | Skill | Saves to |
|---|---|---|
| 1. Find a topic | `topic-discovery` | `01-topic.md` |
| 2. Literature review | `literature-review` | `02-literature-review.md` |
| 3. Research question | `research-question` | `03-research-question.md` |
| 4. Methodology | `methodology-design` | `04-methodology.md` |
| 5. Analysis and results | `analysis-and-results` | `05-results.md` |
| 6. Paper draft | `paper-writing` | `06-draft.md` |
| 7. Final review | `final-review` | `07-review.md` |

All files go in `research/<project-slug>/`, and `00-state.md` in that folder tracks where the project is.

## Install

You need [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) and Python 3 (standard library only, no packages to install).

Copy the `.claude` folder from this repo into your project root to use it in that project, or into `~/.claude` to use it everywhere.

```bash
git clone https://github.com/Alif416/claude-research-agent.git
cp -r claude-research-agent/.claude /path/to/your/project/
```

Restart Claude Code and run `/agents` to check that `research-agent` is listed.

## Use

```
Use the research-agent to find a topic in <your research area>
Use the research-agent to do the literature review on <your topic>
Use the research-agent to continue the project
```

The last one reads `research/<project-slug>/00-state.md` and picks up from the last finished stage.

## How the literature review finds papers

The `literature-review` skill has two small scripts in `.claude/skills/literature-review/scripts/`:

```bash
python3 search_arxiv.py "your query" --max 15
python3 search_semantic_scholar.py "your query" --max 15 --year 2021-
```

They print one JSON object per paper. The agent also uses web search for journal papers and dataset pages. Semantic Scholar limits anonymous requests, so set `S2_API_KEY` in your environment if you hit rate limits.

## Rules the agent follows

- It never invents a paper, number, quote or result. Every citation must come from a search it actually ran, and anything it could not verify is marked `[unverified]`.
- If a tool fails or returns nothing, it says so.
- It writes in plain language, without filler.

## Notes

- If your Claude Code version supports it, `claude --agent research-agent` runs the whole session as this agent, so it can ask you questions directly.
- The `skills:` line in the agent file preloads the skills. If your version ignores it, the skills still load on their own because their descriptions match each stage.
- The skills are plain text. Edit them to fit your field, your venue, and your own writing style.

## Contributing

Issues and pull requests are welcome, especially new field-specific versions of the skills (medicine, social science, and so on).

## License

MIT. See [LICENSE](LICENSE).
