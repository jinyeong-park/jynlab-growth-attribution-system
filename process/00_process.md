# Growth Attribution System — End-to-End Process Guide

> **Purpose:** A step-by-step walkthrough of the entire pipeline from data acquisition to marketing decisions.
> Anyone in a Data Analyst, Marketing Analyst, or Growth Analyst role can follow this guide to reproduce the project from scratch.

---

## The Big Picture

```
[Data Acquisition] → [Data Cleaning] → [Attribution Modeling] → [Geo Experiment] → [Decision]
     PHASE 1              PHASE 2             PHASE 3               PHASE 4          PHASE 5
```

```
Ad Platform APIs      SQL LOWER()         First-Touch SQL       Geo-Holdout        Budget
(Meta / Google /  →   UTM normalization → Last-Touch SQL    →   Experiment     →   Reallocation
 TikTok)              Deduplication       Time-Decay SQL         iCAC Calculation   ROI Reporting
GA4 / Segment
Backend DB
```

---

## Phase Overview

| Phase | What Happens | Primary Role | Deep-Dive File |
|-------|--------------|--------------|----------------|
| 1 | Data Acquisition — How real companies collect ad and conversion data | All roles | [01_data_acquisition.md](./01_data_acquisition.md) |
| 2 | Data Cleaning — Removing noise and standardizing raw data with SQL | Data Analyst | [02_data_cleaning_sql.md](./02_data_cleaning_sql.md) |
| 3 | Attribution Modeling — Calculating channel-level conversion credit | Data Analyst / Data Scientist | [03_attribution_models_sql.md](./03_attribution_models_sql.md) |
| 4 | Geo-Holdout Experiment — Measuring true incremental lift with Python | Data Scientist / Growth Analyst | [04_geo_holdout_python.md](./04_geo_holdout_python.md) |
| 5 | Marketing Insights & Decisions — Interpreting results and adjusting budgets | Marketing Analyst / Growth Lead | [05_marketing_insights.md](./05_marketing_insights.md) |

---

## Reading Guide by Role

You do not need to read everything. Start with the section most relevant to your role.

### Marketing Analyst / Growth Marketer
> Focused on interpreting results and setting channel strategy.

**Recommended order:** Phase 1 (conceptual overview) → Phase 5 (decision-making) → Phase 3 (understand why the numbers differ)

1. [01_data_acquisition.md](./01_data_acquisition.md) — Understand where the data comes from at a high level
2. [05_marketing_insights.md](./05_marketing_insights.md) — The most important file: ROAS, iCAC, budget reallocation
3. [03_attribution_models_sql.md](./03_attribution_models_sql.md) — Why each attribution model produces different numbers

### Data Analyst
> Focused on cleaning data and building attribution models in SQL.

**Recommended order:** Follow phases 1 through 3 in order.

1. [01_data_acquisition.md](./01_data_acquisition.md)
2. [02_data_cleaning_sql.md](./02_data_cleaning_sql.md) — Core SQL cleaning patterns
3. [03_attribution_models_sql.md](./03_attribution_models_sql.md) — Window functions and MTA logic

### Data Scientist / Growth Analyst
> Focused on experiment design and statistical validation.

**Recommended order:** Skim phases 1–3, then focus on Phase 4.

1. [01_data_acquisition.md](./01_data_acquisition.md)
2. [03_attribution_models_sql.md](./03_attribution_models_sql.md) — Understand why SQL attribution alone is insufficient
3. [04_geo_holdout_python.md](./04_geo_holdout_python.md) — Experiment design and Python incrementality code

---

## Key Terms Glossary

| Term | Plain-English Definition |
|------|--------------------------|
| **Attribution** | The process of assigning credit to marketing channels for driving a conversion |
| **Multi-Touch Attribution (MTA)** | A class of models that distribute conversion credit across all touchpoints in the user journey, not just the first or last click |
| **Self-Attribution Bias** | Each ad platform (Meta, Google) independently claims credit for the same conversion, leading to double-counting |
| **ROAS** | Return on Ad Spend — revenue generated per dollar of ad spend |
| **iCAC** | Incremental Cost per Acquisition — cost to acquire one additional customer that would not have converted organically |
| **Geo-Holdout** | An experiment where ads are paused in a subset of geographic markets (control) to measure the baseline conversion rate vs. markets where ads remain active (treatment) |
| **DMA** | Designated Market Area — a U.S. regional advertising market unit (e.g., NYC, LA, Chicago) |
| **UTM Parameters** | Tracking tags appended to URLs that identify how users arrived at a site (utm_source, utm_medium, utm_campaign) |
| **ETL / ELT** | Extract-Transform-Load — the pipeline that moves data from source systems into a data warehouse |
| **CDC** | Change Data Capture — technology that detects and replicates database changes in real time |
| **Attribution Window** | The lookback period used to determine which touchpoints are eligible for attribution credit (e.g., 7-day, 30-day) |

---

## The Core Problem This Project Solves

```
The Problem:
  Meta Ads Manager  reports → "We drove 350 conversions"
  Google Ads        reports → "We drove 280 conversions"
  Actual total conversions → 420

  Each platform independently claims credit for the same conversion events.
  Combined platform-reported conversions exceed real conversions by 34%.
  This inflated view leads to misallocating budget toward low-performing channels.

The Solution:
  Step 1 — SQL Multi-Touch Attribution: deduplicate touchpoints and distribute
            conversion credit across channels using verifiable clickstream data.
  Step 2 — Geo-Holdout Experiment: pause Meta ads in 10 control DMAs to measure
            how many conversions happen organically (without any Meta ad).
  Step 3 — Reallocate $100K from low-incrementality Meta retargeting
            toward high-incrementality Google Search and TikTok prospecting.
```

---

## Final Results Summary

| Channel | Platform-Reported ROAS | True Incremental ROAS | Action Taken |
|---------|------------------------|----------------------|--------------|
| Meta Paid Social | 3.25x | **1.26x** | Budget cut — high organic cannibalization |
| Google Paid Search | 2.80x | **2.65x** | Budget increased — high incremental lift |
| TikTok Ads | 1.60x | **2.10x** | Budget increased — strong new-user acquisition |
| Blended Total | 2.80x | **1.91x** | $100K reallocated; Blended CAC fell 14.2% |

> Meta appeared to be the top performer based on platform reporting.
> In reality, it was the lowest-incrementality channel — over 60% of its attributed
> conversions would have happened anyway through Organic Search or Direct.

---

*Follow the links in the Phase Overview table to read each section in detail.*
