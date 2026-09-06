# 🎯 Multi-Touch Attribution & Geo-Incrementality Engine

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.0-4169E1?style=flat-square&logo=postgresql)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

An end-to-end growth analytics system that uncovers true campaign ROI by resolving ad platform over-reporting, modeling multi-touch attribution (MTA) in SQL, and running matched-market geo-incrementality testing in Python.

---

## 📌 Executive Summary

Modern ad platforms (Meta, Google, TikTok) often over-report conversion metrics due to self-attribution bias and overlapping cookie windows. This project addresses the post-iOS 14 signal loss by building a **deterministic clickstream attribution model** alongside a **matched-market geo-holdout experiment**.

* **Key Finding:** Platform-reported conversions over-estimated paid social ROI by **38%** due to duplicate attribution across Meta and Google Search.
* **Business Impact:** Reallocated **$100,000** in quarterly spend from saturated Meta retargeting campaigns to high-incrementality Google Search & TikTok prospecting, lowering overall Blended CAC by **14.2%** while maintaining total acquisition volume.

---

## 🏗️ System Architecture & Data Flow
[Raw Ad Spend Logs]
│
▼
[PostgreSQL Pipeline] ──> [SQL MTA Models] ──> [Geo-Holdout Test] ──> [Streamlit Executive App]
[User Touchpoint Logs] / (Cleaning & Deduplication) (First/Last/Decay) (Incrementality Lift) (Decision Dashboard)

text

1. **Ingestion & Cleaning:** Ingests raw cross-channel event logs and handles data anomalies (missing UTMs, inconsistent case naming, and duplicate timestamps).
2. **Attribution Engine (SQL):** Runs window-function-driven models (First-Touch, Last-Touch, Linear, Time-Decay) to re-attribute conversion touchpoints.
3. **Incrementality Engine (Python):** Analyzes a 30-day matched-market geo-holdout test across 50 Designated Market Areas (DMAs) to measure baseline vs. incremental conversion lift.
4. **Interactive Dashboard:** Deploys a Streamlit application mapping **Attributed ROAS vs. Incremental ROAS** for marketing executive decision-making.

---

## 📊 Key Analytical Findings

| Attribution Model | Meta Ad Spend Share | Meta Attributed Revenue | Implied ROAS | Key Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| **Platform Reported** | 45.0% | $245,000 | **3.25x** | Severe over-crediting due to 7-day view-through window. |
| **First-Touch (SQL)** | 45.0% | $180,000 | **2.38x** | High efficiency at top-of-funnel brand discovery. |
| **Last-Touch (SQL)** | 45.0% | $110,000 | **1.46x** | Captures users already intending to convert; low incremental value. |
| **Time-Decay (SQL)** | 45.0% | $142,000 | **1.88x** | Balanced view reflecting multi-channel touchpoint decay. |
| **Geo-Incrementality** | 45.0% | $95,000 | **1.26x (True)** | **True Incremental ROAS.** Turning off retargeting in Control DMAs revealed 60%+ organic baseline retention. |

---

## 🛠️ Technical Highlights & Code Samples

### 1. Advanced SQL Window Functions for Touchpoint Sequence

The SQL pipeline utilizes CTEs and PostgreSQL window functions (`ROW_NUMBER`, `FIRST_VALUE`, `LAG`) to map out chronological user journeys and assign time-decay weights:

```sql
WITH touchpoint_sequencing AS (
    SELECT 
        user_id,
        event_id,
        channel,
        timestamp,
        order_value_usd,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp ASC) AS touchpoint_order,
        COUNT(*) OVER (PARTITION BY user_id) AS total_touchpoints,
        EXTRACT(EPOCH FROM (MAX(timestamp) OVER (PARTITION BY user_id) - timestamp)) / 86400.0 AS days_before_conversion
    FROM user_touchpoint_events
    WHERE user_id IN (SELECT user_id FROM user_touchpoint_events WHERE event_type = 'purchase')
),
time_decay_weights AS (
    SELECT 
        user_id,
        channel,
        order_value_usd,
        -- Exponential decay formula with a 7-day half-life: 2^(-days / 7)
        POW(2, -days_before_conversion / 7.0) AS weight
    FROM touchpoint_sequencing
)
SELECT 
    channel,
    ROUND(SUM(order_value_usd * (weight / total_weight_per_user)), 2) AS time_decay_attributed_revenue
FROM (
    SELECT *, SUM(weight) OVER (PARTITION BY user_id) AS total_weight_per_user 
    FROM time_decay_weights
) t
GROUP BY channel
ORDER BY time_decay_attributed_revenue DESC;
2. Geo-Holdout Incrementality & Lift Calculation (Python)
Evaluates treatment DMAs (Meta ads active) vs. control DMAs (Meta ads turned off for 30 days) to compute true Incremental Cost Per Acquisition (iCAC):

python
import pandas as pd
import numpy as np

def calculate_geo_incrementality(df_treatment: pd.DataFrame, df_control: pd.DataFrame, ad_spend: float):
    """
    Calculates incremental lift and true iCAC using Matched-Market Geo Testing.
    """
    baseline_conversion_rate = df_control['conversions'].sum() / df_control['population'].sum()
    expected_control_conversions = df_treatment['population'].sum() * baseline_conversion_rate
    actual_treatment_conversions = df_treatment['conversions'].sum()
    
    incremental_conversions = actual_treatment_conversions - expected_control_conversions
    incremental_cac = ad_spend / incremental_conversions if incremental_conversions > 0 else np.inf
    
    return {
        "expected_baseline_conversions": round(expected_control_conversions, 0),
        "actual_conversions": actual_treatment_conversions,
        "incremental_conversions": round(incremental_conversions, 0),
        "incremental_cac_usd": round(incremental_cac, 2)
    }
📂 Repository Structure
text
├── data/
│   ├── raw_ad_spend.csv              # Synthetic spend & platform-reported logs
│   └── user_touchpoint_events.csv    # Clickstream event logs with injected data noise
├── sql/
│   ├── 01_data_cleaning.sql          # UTM harmonization & case sensitivity fixes
│   ├── 02_first_last_touch.sql       # First-touch & Last-touch SQL models
│   └── 03_time_decay_attribution.sql # Time-decay window function logic
├── scripts/
│   ├── generate_synthetic_data.py    # Python script simulating 6 months of ad data
│   └── run_incrementality_test.py    # Geo-holdout Statistical Analysis script
├── app/
│   └── app.py                        # Streamlit interactive executive dashboard
├── docs/
│   └── tracking_plan.md              # Event taxonomy & Tracking spec sheet
├── requirements.txt                  # Python dependency specifications
└── README.md                         # Project documentation
⚡ Quickstart & Reproducibility
Clone the repository:

bash
git clone https://github.com/jinyeong-park/jynlab-growth-attribution-system.git
cd jynlab-growth-attribution-system
Set up Python Virtual Environment & Install Dependencies:

bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Generate Synthetic Datasets:

bash
python scripts/generate_synthetic_data.py
Run Streamlit Executive Dashboard:

bash
streamlit run app/app.py
📬 Contact & Connect
Jenny Park — Marketing & Growth Analytics Specialist

📍 Location: San Jose, California
💼 LinkedIn: linkedin.com/in/jennypark7

✉️ Email: byjennypark@gmail.com

