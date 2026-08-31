# Paid acquisition & attribution system

I'm Jenny Park. I built this to answer one question I kept running into: platforms report clicks and impressions, but almost never tell you whether the money you spent actually produced a customer worth having.

This is a paid search growth system — campaign strategy, conversion architecture, attribution, and an AI-agent playbook — that I designed and I'm running with real ad spend on a real product I own, [FirstHomeBayArea](https://firsthomebayarea.com). I built it to be vertical-agnostic on purpose: the mechanics here (real conversion definitions instead of vanity metrics, incrementality testing, funnel-stage attribution) are the same mechanics a B2B SaaS growth or paid media role runs, just applied to a real estate product because that's the real product I had.

**Status: active.** Campaign is live as of [DATE]. Numbers below get filled in as real data comes in — nothing here is backfilled or simulated.

---

## Why FirstHomeBayArea

FirstHomeBayArea helps first-time Bay Area buyers evaluate condos — HOA health, true monthly cost, comparable sales — instead of just showing listings. It has a real affordability calculator, real traffic, and a defined primary conversion (an "Email My Results" request, not a button click). That gave me a real funnel to instrument, not a synthetic dataset.

Full product context: [`campaign/README.md`](campaign/README.md).

## What's in this repo

| Folder | What it is |
|---|---|
| [`campaign/`](campaign/) | Keyword strategy, targeting, ad copy, and the reasoning behind them |
| [`attribution/`](attribution/) | How I define and measure a real conversion — CAC, funnel-stage conversion rates, SQL/Python analysis |
| [`incrementality/`](incrementality/) | A lightweight on/off lift test — did the ads cause the conversions, or would they have happened anyway |
| [`segmentation/`](segmentation/) | Treating keyword themes as a mini market portfolio, to decide what to scale first |
| [`ai-agent-playbook/`](ai-agent-playbook/) | Four reusable AI-assisted workflows (research, content, performance reporting, experiment prioritization) with actual prompts and logs, not just descriptions |
| [`case-study/`](case-study/) | The executive summary, and the explicit mapping of this funnel onto a standard B2B SaaS funnel (MQL → SQL → pipeline) |

## Tech stack

Google Ads · Google Ads API · GA4 · SQL · Python (pandas) · Claude (Anthropic) for the agent playbook

## Why this matters for a B2B SaaS growth role

Every mechanic here transfers directly:

- **Real conversion, not vanity metrics** → the same discipline a Growth PM needs when a platform reports "conversions" that don't tie to pipeline.
- **Incrementality testing** → the same question enterprise marketing teams ask about attribution beyond last-click.
- **Keyword themes as a portfolio** → the same logic as managing a book of accounts or campaigns and deciding where to allocate budget next.
- **AI agent playbook** → workflows built and documented well enough that someone else on a team could run them, not one-off prompting.

The full translation table (this funnel's stages mapped to Visitor → MQL → SQL → Opportunity) is in [`case-study/README.md`](case-study/README.md).

## About me

I'm transitioning into Data/Business Analyst and Growth/Paid Media roles in the Bay Area, building on a background in program management (SAP, Gulf Air multi-country operations) and technical training (Hack Reactor — Python, SQL, JS). I also run [JYNLAB](https://jynlab.com). This project, and my [B2B SaaS Data & Business Analytics project](https://github.com/jinyeong-park/jynlab-b2b-saas-analytics), are the two things I point to when someone asks "what have you actually built."
