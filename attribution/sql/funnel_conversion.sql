-- Funnel stage conversion and drop-off, by keyword theme.
-- Source: GA4 export (BigQuery events table) joined to Google Ads campaign/ad group
-- via the utm_campaign / utm_content parameters set on each ad group's final URL.
--
-- Replace `events_*` with the actual GA4 BigQuery export table for the property.

WITH stage_events AS (
    SELECT
        user_pseudo_id,
        event_name,
        event_timestamp,
        (SELECT value.string_value FROM UNNEST(event_params)
            WHERE key = 'campaign_theme') AS keyword_theme
    FROM `firsthomebayarea.analytics_XXXXXXXXX.events_*`
    WHERE event_name IN (
        'affordability_calculator_started',
        'affordability_calculator_completed',
        'affordability_result_email_cta_clicked',
        'affordability_result_email_submitted'
    )
),

funnel_summary AS (
    SELECT
        keyword_theme,
        COUNT(DISTINCT CASE WHEN event_name = 'affordability_calculator_started'
            THEN user_pseudo_id END) AS started,
        COUNT(DISTINCT CASE WHEN event_name = 'affordability_calculator_completed'
            THEN user_pseudo_id END) AS completed,
        COUNT(DISTINCT CASE WHEN event_name = 'affordability_result_email_cta_clicked'
            THEN user_pseudo_id END) AS cta_clicked,
        COUNT(DISTINCT CASE WHEN event_name = 'affordability_result_email_submitted'
            THEN user_pseudo_id END) AS converted
    FROM stage_events
    GROUP BY keyword_theme
)

SELECT
    keyword_theme,
    started,
    completed,
    cta_clicked,
    converted,

    ROUND(100.0 * completed / NULLIF(started, 0), 2)      AS start_to_complete_rate,
    ROUND(100.0 * cta_clicked / NULLIF(completed, 0), 2)   AS complete_to_cta_rate,
    ROUND(100.0 * converted / NULLIF(cta_clicked, 0), 2)   AS cta_to_conversion_rate,
    ROUND(100.0 * converted / NULLIF(started, 0), 2)       AS overall_conversion_rate

FROM funnel_summary
ORDER BY overall_conversion_rate DESC;
