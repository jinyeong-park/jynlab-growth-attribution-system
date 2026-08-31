-- Real cost-per-conversion (spend / "Email My Results" submissions), blended and by
-- keyword theme. This is the number that decides budget reallocation, not Google's
-- default cost-per-conversion, which is allowed to count softer events.
--
-- Source: Google Ads API report (campaign/ad group cost) joined to the conversion
-- counts from funnel_conversion.sql via keyword_theme.

WITH ad_spend AS (
    SELECT
        keyword_theme,
        SUM(cost_micros) / 1e6 AS spend_usd,
        SUM(clicks) AS clicks,
        SUM(impressions) AS impressions
    FROM `google_ads_export.ad_group_performance`
    GROUP BY keyword_theme
),

conversions AS (
    SELECT
        keyword_theme,
        converted AS real_conversions
    FROM funnel_conversion  -- output of funnel_conversion.sql, materialized as a table/view
)

SELECT
    s.keyword_theme,
    s.spend_usd,
    s.clicks,
    s.impressions,
    ROUND(s.spend_usd / NULLIF(s.clicks, 0), 2)       AS avg_cpc,
    ROUND(100.0 * s.clicks / NULLIF(s.impressions, 0), 2) AS ctr_pct,
    c.real_conversions,
    ROUND(s.spend_usd / NULLIF(c.real_conversions, 0), 2) AS cost_per_real_conversion

FROM ad_spend s
JOIN conversions c USING (keyword_theme)
ORDER BY cost_per_real_conversion ASC;
