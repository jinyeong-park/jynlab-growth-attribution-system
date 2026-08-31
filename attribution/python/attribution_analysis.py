"""
Pulls Google Ads spend/click data and GA4 funnel-event data, joins them by keyword
theme, and produces the cost-per-real-conversion and funnel drop-off tables used in
../../case-study/. Mirrors the logic in ../sql/, but as a script so it can also
generate the charts for the case study.

Usage:
    python attribution_analysis.py --start 2026-XX-XX --end 2026-XX-XX

Inputs (see README for how each is obtained):
    - Google Ads report export (CSV or via google-ads API client) with columns:
      date, campaign, ad_group, keyword_theme, cost_micros, clicks, impressions
    - GA4 BigQuery export or GA4 API export with the five funnel events defined
      in ../README.md

Status: written against the schema below; not yet run against live data.
Real numbers land here once the campaign has at least one full week of spend.
"""

import argparse
import pandas as pd


FUNNEL_EVENTS = [
    "affordability_calculator_started",
    "affordability_calculator_completed",
    "affordability_result_email_cta_clicked",
    "affordability_result_email_submitted",
]


def load_ads_report(path: str) -> pd.DataFrame:
    """Google Ads performance export, one row per campaign/ad_group/date."""
    df = pd.read_csv(path)
    df["spend_usd"] = df["cost_micros"] / 1e6
    return df


def load_ga4_events(path: str) -> pd.DataFrame:
    """GA4 event export, one row per event occurrence."""
    df = pd.read_csv(path)
    return df[df["event_name"].isin(FUNNEL_EVENTS)]


def funnel_by_theme(events: pd.DataFrame) -> pd.DataFrame:
    pivot = (
        events
        .drop_duplicates(subset=["user_pseudo_id", "event_name", "keyword_theme"])
        .groupby(["keyword_theme", "event_name"])["user_pseudo_id"]
        .nunique()
        .unstack(fill_value=0)
        .reindex(columns=FUNNEL_EVENTS, fill_value=0)
    )
    pivot.columns = ["started", "completed", "cta_clicked", "converted"]
    pivot["start_to_complete_rate"] = pivot["completed"] / pivot["started"].replace(0, pd.NA)
    pivot["complete_to_cta_rate"] = pivot["cta_clicked"] / pivot["completed"].replace(0, pd.NA)
    pivot["cta_to_conversion_rate"] = pivot["converted"] / pivot["cta_clicked"].replace(0, pd.NA)
    pivot["overall_conversion_rate"] = pivot["converted"] / pivot["started"].replace(0, pd.NA)
    return pivot.reset_index()


def cost_per_real_conversion(ads: pd.DataFrame, funnel: pd.DataFrame) -> pd.DataFrame:
    spend = ads.groupby("keyword_theme").agg(
        spend_usd=("spend_usd", "sum"),
        clicks=("clicks", "sum"),
        impressions=("impressions", "sum"),
    ).reset_index()

    merged = spend.merge(funnel[["keyword_theme", "converted"]], on="keyword_theme", how="left")
    merged["avg_cpc"] = merged["spend_usd"] / merged["clicks"].replace(0, pd.NA)
    merged["ctr_pct"] = 100 * merged["clicks"] / merged["impressions"].replace(0, pd.NA)
    merged["cost_per_real_conversion"] = merged["spend_usd"] / merged["converted"].replace(0, pd.NA)
    return merged.sort_values("cost_per_real_conversion")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ads-export", default="data/google_ads_export.csv")
    parser.add_argument("--ga4-export", default="data/ga4_events_export.csv")
    args = parser.parse_args()

    ads = load_ads_report(args.ads_export)
    events = load_ga4_events(args.ga4_export)

    funnel = funnel_by_theme(events)
    print("\nFunnel by keyword theme:\n", funnel)

    performance = cost_per_real_conversion(ads, funnel)
    print("\nCost per real conversion by keyword theme:\n", performance)

    funnel.to_csv("output_funnel_by_theme.csv", index=False)
    performance.to_csv("output_cost_per_conversion.csv", index=False)


if __name__ == "__main__":
    main()
