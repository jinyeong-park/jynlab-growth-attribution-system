# AI agent playbook

Four reusable AI-assisted workflows I use to run this campaign, written down well enough that someone else could pick one up and run it — not one-off prompting I can't reproduce.

Each file below has: what the agent is for, the actual prompt template (with placeholders), an example run, and where a human has to check its work before anything ships. AI drafts here; I own the decision.

| Agent | Used for | File |
|---|---|---|
| Research | Keyword and competitor research before a campaign or theme launches | [`research-agent.md`](research-agent.md) |
| Content | First-draft ad copy, then edited by hand | [`content-agent.md`](content-agent.md) |
| Performance | Weekly read of the numbers, translated into a kill/scale/hold call | [`performance-agent.md`](performance-agent.md) |
| Experiment | Turning this week's findings into next week's prioritized test | [`experiment-agent.md`](experiment-agent.md) |

## Ground rules

- The agent never sees raw financial or PII data — inputs are aggregated metrics only (spend, clicks, conversion counts), consistent with what actually gets logged in [`../attribution/`](../attribution/).
- Every AI-generated recommendation gets a human decision logged next to it. If I didn't follow the suggestion, the log says why.
- No agent output goes live (ad copy, budget change) without me reviewing it first.
