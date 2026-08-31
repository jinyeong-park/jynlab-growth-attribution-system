# Incrementality test

## The question

Cost-per-conversion tells you what you spent per conversion. It doesn't tell you whether the ads *caused* those conversions or whether the same people would have found FirstHomeBayArea anyway through organic search or direct traffic. Platform-reported attribution has no reason to tell you this — it's graded on its own homework.

## Design (small-budget version)

A full geo-holdout test needs more spend and traffic than this campaign has. Instead, this is a time-based on/off test, which is the honest, budget-appropriate version of the same idea:

1. **Week 1–2**: campaign live, normal spend.
2. **Week 3**: campaign paused entirely.
3. **Week 4**: campaign live again.

For each week, track:
- Organic + direct sessions to `/affordability`
- "Email My Results" conversions from organic/direct traffic only

If organic/direct conversions stay flat whether the campaign is on or off, that's evidence the paid conversions are close to fully incremental. If organic/direct conversions rise noticeably in the off week, some of what the ads were "getting credit for" would have happened anyway.

## Limitation, stated plainly

Two on/off cycles on one small campaign is a signal, not a rigorous causal estimate — seasonality, day-of-week effects, and small sample size all confound it. The point of including this isn't to claim statistical rigor I don't have the budget for. It's to show the instinct: don't take a platform's attribution at face value, and design the cheapest test that gives you a real read. At scale (the kind of budget a company like OpenArt or Okara runs), the same logic becomes a proper geo-holdout or matched-market test — described in [`../case-study/README.md`](../case-study/README.md).

## Results

[TODO — fill in after the four-week cycle completes.]
