# Performance agent

**Use for**: the weekly read of the numbers — translating a table of metrics into a plain-English kill/scale/hold recommendation, before I make the actual budget call.

## Prompt template

```
Here is this week's performance by keyword theme for a Google Search Ads
campaign (real numbers, not platform-reported vanity conversions — "converted"
below means a confirmed "Email My Results" submission):

[PASTE OUTPUT OF attribution/python/attribution_analysis.py OR THE SQL RESULTS —
spend, clicks, impressions, avg_cpc, ctr_pct, converted, cost_per_real_conversion,
per theme, plus this week vs. last week]

For each theme, tell me:
1. Kill, scale, or hold — and the one number that drove that call.
2. What would have to be true for you to be wrong about that call (e.g. small
   sample size, a seasonal effect, one outlier day).
3. One thing you'd want to know that isn't in this data before committing real
   budget to your recommendation.

Do not recommend a budget change based on fewer than [N] conversions per theme —
say so explicitly if the sample is too small to call.
```

## Example run

[TODO — paste the first real weekly run here, plus my actual decision and whether I followed the recommendation.]

## Human check required

- I make the actual budget change, not the agent — this produces a recommendation and a confidence check, not an action.
- Small-sample weeks get held, not acted on, regardless of what the raw number looks like.
