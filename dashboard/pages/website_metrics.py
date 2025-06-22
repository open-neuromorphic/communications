
# website_metrics.py

import streamlit as st
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.auth import default
import os

def format_number(n):
    return f"{n:,}"

st.set_page_config(page_title="Website Performance & Engagement", layout="wide")
st.title("🌐 Website Performance & Engagement")

try:
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/analytics.readonly"])
    client = BetaAnalyticsDataClient(credentials=credentials)
    property_id = os.getenv("GA4_PROPERTY_ID")

    st.subheader("📈 Sessions")
    sessions_request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[],
        metrics=[Metric(name="sessions")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")]
    )
    sessions_response = client.run_report(sessions_request)
    sessions = int(sessions_response.rows[0].metric_values[0].value)
    st.metric("Total Sessions (Last 30 Days)", format_number(sessions))

    st.subheader("⏱️ Engagement Time & Rate")
    engagement_request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[],
        metrics=[
            Metric(name="averageSessionDuration"),
            Metric(name="engagementRate")
        ],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")]
    )
    engagement_response = client.run_report(engagement_request)
    avg_time = float(engagement_response.rows[0].metric_values[0].value)
    engagement_rate = float(engagement_response.rows[0].metric_values[1].value)

    col1, col2 = st.columns(2)
    col1.metric("Avg. Engagement Time (s)", f"{avg_time:.1f}")
    col2.metric("Engagement Rate (%)", f"{engagement_rate * 100:.2f}%")

    st.subheader("📄 Top Landing Pages")
    landing_request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="landingPagePlusQueryString")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="averageSessionDuration")
        ],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")]
    )
    landing_response = client.run_report(landing_request)

    landing_data = [
        {
            "Page": row.dimension_values[0].value,
            "Sessions": int(row.metric_values[0].value),
            "Avg. Engagement Time (s)": float(row.metric_values[1].value)
        }
        for row in landing_response.rows
    ]
    st.dataframe(landing_data)

except Exception as e:
    st.error(f"Error loading website engagement metrics: {e}")
