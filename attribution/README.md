# Attribution and measurement

## The problem this solves

Google Ads will happily report "conversions" on a calculator button click. That number goes up even if nobody who clicked it ever became a real lead. Cost-per-click and cost-per-platform-conversion are vanity metrics if the conversion event isn't tied to something the business actually wants.

So before any ad spend, I defined the real conversion and built tracking around it — documented in the FirstHomeBayArea codebase's own readiness work (three P0 requirements: conversion tracking wired to Google Ads, a proper GA4 event schema for the calculator funnel, and a dedicated "Email My Results" capture flow, replacing the generic newsletter form that used to sit there).

## Funnel stages tracked

1. `affordability_calculator_started` — first meaningful interaction, not every keystroke
2. `affordability_calculator_completed` — enough valid inputs to produce a result
3. `affordability_result_email_cta_clicked` — clicked the "Email My Results" CTA
4. `affordability_result_email_submitted` — **the real conversion** (only fires after a confirmed server-side save, not on click)
5. `affordability_result_email_failed` — submission attempted but failed (matters for diagnosing lost conversions that aren't the campaign's fault)

Privacy note: household income, monthly debt, and email address never get sent to GA4 as event parameters — only non-sensitive metadata (source page, result band, has-HOA, down-payment range).

## What I calculate

- **Cost per real conversion** (spend ÷ stage-4 events) — the number that actually matters, reported alongside and instead of Google's default cost-per-conversion.
- **Stage-to-stage conversion rate** — where the funnel actually leaks (e.g., calculator completed → email submitted is usually the real drop-off, not started → completed).
- **Cost per real conversion by keyword theme** — see [`../campaign/README.md`](../campaign/README.md) for the three themes; this is the number that decides where budget goes next.
- **Click-attributed vs. view-attributed performance**, reported separately rather than blended, since blending is how platforms make display and remarketing look more effective than they are.

## Files

- [`sql/funnel_conversion.sql`](sql/funnel_conversion.sql) — stage-by-stage conversion and drop-off, by keyword theme
- [`sql/cost_per_conversion.sql`](sql/cost_per_conversion.sql) — real cost-per-conversion, blended and by theme
- [`python/attribution_analysis.py`](python/attribution_analysis.py) — pulls Google Ads + GA4 exports, joins them, produces the tables above and the charts used in [`../case-study/`](../case-study/)

## Status

[TODO — replace this section with actual numbers once the campaign has run for at least one full week. Until then, the queries and script above are written against the event schema but not yet run against live data.]
