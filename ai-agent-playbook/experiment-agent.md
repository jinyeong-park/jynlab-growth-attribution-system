# Experiment agent

**Use for**: turning this week's findings into next week's single, well-scoped test — so testing is prioritized, not just "let's also try this."

## Prompt template

```
This week's findings:
[SUMMARY FROM performance-agent.md OUTPUT]

Open questions I have:
[e.g. "Is Theme B underperforming because of copy, or because the audience
genuinely converts worse?" / "Would a landing page variant that leads with the
HOA angle instead of the calculator change the completion rate?"]

Propose 3 candidate experiments for next week. For each:
1. The specific hypothesis (if X, then Y, because Z).
2. What I'd change (one variable only — copy, landing page, bid strategy,
   audience — not several at once).
3. The minimum sample size or time window before I can read a result.
4. How this experiment would change the segmentation table in
   segmentation/README.md if it wins.

Rank the 3 by expected impact on cost-per-real-conversion, not by how
interesting the test is.
```

## Example run

[TODO — paste the first real run here, and which of the 3 candidates I actually ran and why.]

## Human check required

- I pick which one experiment actually runs — one at a time, so results stay readable.
- "Expected impact" ranking is a starting point for my judgment, not a substitute for it.
