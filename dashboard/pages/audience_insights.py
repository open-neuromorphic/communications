
from pathlib import Path
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric
import pandas as pd
import os
from google.oauth2 import service_account
import streamlit as st

# Helper function
def run_ga4_report(client, property_id, dimensions, metrics):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        date_ranges=[{"start_date": "30daysAgo", "end_date": "today"}],
    )
    response = client.run_report(request)
    rows = response.rows or []
    return pd.DataFrame([{**{d.name: v for d, v in zip(response.dimension_headers, r.dimension_values)},
                          **{m.name: v for m, v in zip(response.metric_headers, r.metric_values)}} for r in rows])

# Authenticate
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
credentials = service_account.Credentials.from_service_account_file(
    os.getenv("GSC_SERVICE_ACCOUNT_PATH"), scopes=SCOPES
    )
client = BetaAnalyticsDataClient(credentials=credentials)
property_id = os.getenv("GA4_PROPERTY_ID")

# --- Top Countries ---
print("\n📍 Top Countries (Users, Engagement Rate):")
df_countries = run_ga4_report(client, property_id, ["country"], ["activeUsers", "engagementRate"])
print(df_countries)

# --- Device Categories ---
print("\n📱 Device Category Breakdown:")
df_devices = run_ga4_report(client, property_id, ["deviceCategory"], ["activeUsers"])
print(df_devices)

# --- Top Browsers & Operating Systems ---
print("\n🌐 Top Browsers:")
df_browsers = run_ga4_report(client, property_id, ["browser"], ["activeUsers"])
print(df_browsers)

print("\n💻 Top Operating Systems:")
df_os = run_ga4_report(client, property_id, ["operatingSystem"], ["activeUsers"])
print(df_os)
# Streamlit page setup
st.set_page_config(page_title="Audience Insights", layout="wide")

st.title("📊 Audience Insights")

# --- Top Countries ---
st.subheader("📍 Top Countries (Users, Engagement Rate):")
st.dataframe(df_countries)

# --- Device Categories ---
st.subheader("📱 Device Category Breakdown:")
st.dataframe(df_devices)

# --- Top Browsers & Operating Systems ---
st.subheader("🌐 Top Browsers:")
st.dataframe(df_browsers)

st.subheader("💻 Top Operating Systems:")
st.dataframe(df_os)