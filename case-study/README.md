# Case study and B2B SaaS funnel mapping

## Executive summary

[TODO — fill in once the campaign has run its full cycle. Format below; nothing gets filled in until it's a real, checkable number.]

- **Budget**: $[TODO] over [TODO] weeks
- **Real conversions** (confirmed "Email My Results" requests): [TODO]
- **Cost per real conversion**: $[TODO], vs. $[TODO] platform-reported cost-per-conversion (the gap between these two numbers is itself a finding — see [`../attribution/README.md`](../attribution/README.md))
- **Winning keyword theme**: [TODO], at $[TODO] cost per real conversion vs. $[TODO] for the weakest theme
- **Incrementality read**: [TODO] — see [`../incrementality/README.md`](../incrementality/README.md)
- **What I'd do with a bigger budget**: [TODO]

## Why this exists as a B2B SaaS-relevant project

I built and ran this on FirstHomeBayArea, a real estate product, because it's a real product I own with real traffic and a real defined conversion — not because I'm targeting real estate roles. The table below is the actual point of the project: the mechanics are the same ones a B2B SaaS growth or paid media role runs, just with different funnel-stage names.

| This project | Standard B2B SaaS funnel | Why it's the same mechanic |
|---|---|---|
| Visitor lands on `/affordability` | Visitor / Website traffic | Same top-of-funnel measurement problem: which channel/keyword actually brought them |
| Calculator started | Engaged visitor | First signal of real intent vs. a bounce |
| Calculator completed | Lead | Enough information given voluntarily to count as a real lead, not just traffic |
| "Email My Results" submitted (**primary conversion**) | MQL | The line I refused to draw at a button click — same discipline as refusing to call a form-fill or content download an MQL without an intent signal behind it |
| (Next stage — not yet built) buyer books a consultation / expresses a target price via "My Price" | SQL | Sales-ready signal: specific, actionable intent, not just interest |
| Buyer transacts | Closed-won / Opportunity | Revenue outcome the whole funnel exists to produce |

## What transfers directly to a role at a company like OpenArt, Okara, Eightfold, CommerceIQ, or TikTok's ad business

- **Refusing vanity metrics.** Every one of those job postings specifically calls out the difference between platform-reported numbers and real business outcomes (CAC, LTV, qualified pipeline). [`../attribution/README.md`](../attribution/README.md) is that discipline applied end to end, before a single dollar was spent.
- **Incrementality thinking at whatever budget you actually have.** [`../incrementality/README.md`](../incrementality/README.md) is intentionally honest about what a small-budget test can and can't prove — the same judgment scales up to a geo-holdout or matched-market test with a real team's budget.
- **Portfolio-level budget decisions.** [`../segmentation/README.md`](../segmentation/README.md) treats three keyword themes the way a growth role treats a book of accounts or campaigns: rank by real unit economics, not raw volume, and let the data move the budget.
- **AI as infrastructure, not a demo.** [`../ai-agent-playbook/`](../ai-agent-playbook/) is four documented, reusable workflows with human checkpoints — the exact bar Eightfold's posting sets ("not a prompt button pusher... own and continually expand the team's prompt and agent playbook").

## Honest limitations

- Small budget means the incrementality test and per-theme sample sizes are directional, not statistically rigorous — stated plainly rather than dressed up.
- This is a B2C real estate funnel, not a B2B one. The mapping table above is my argument for why the underlying skill transfers — it's on the reader to judge whether that argument holds, and I'd rather make it explicit than hope no one asks.
- Everything in this repo marked `[TODO]` is genuinely not done yet. Numbers here are real when present, not backfilled.
