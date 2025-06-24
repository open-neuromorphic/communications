# content_performance_with_api.py

import os
import streamlit as st
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric
from pathlib import Path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

# Setup
st.set_page_config(page_title="Content Performance", layout="wide")
st.title("📈 Content Performance: Blog, Workshops, YouTube")

def format_number(n):
    try:
        return f"{int(n):,}"
    except:
        return n

# ----------------------------------------
# Google Analytics 4 API - Blog & Workshop Data
# ----------------------------------------
with st.expander("📝 Blog & Workshop Metrics (GA4)", expanded=True):
    try:
        SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]
        credentials = service_account.Credentials.from_service_account_file(
            os.getenv("GSC_SERVICE_ACCOUNT_PATH"), scopes=SCOPES
            )
        client = BetaAnalyticsDataClient(credentials=credentials)
        property_id = os.getenv("GA4_PROPERTY_ID")

        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name="pagePath")],
            metrics=[
                Metric(name="screenPageViews"),
                Metric(name="userEngagementDuration")
            ],
            date_ranges=[{"start_date": "30daysAgo", "end_date": "today"}],
        )

        response = client.run_report(request)
        rows = response.rows

        table = []
        for row in rows:
            page = row.dimension_values[0].value
            views = row.metric_values[0].value
            duration = round(float(row.metric_values[1].value), 2)

            # Filter specific blog or workshop pages
            if any(x in page for x in [
                "truenorth-deep-dive", "northpole-ibm",
                "spiking-neural-network-framework-benchmarking", "spiking-neurons-digital-hardware",
                "/workshops/", "c-dnn-and-c-transformer", "neuromorphic-intermediate-representation"
            ]):
                table.append((page, views, duration))

        df = pd.DataFrame(table, columns=["Page", "Page Views", "User Engagement Duration (s)"])
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading GA4 blog/workshop metrics: {e}")

# ----------------------------------------
# YouTube Placeholder - Replace with real API calls
# ----------------------------------------
with st.expander("📺 YouTube Video Performance"):
    try:

        # Load YouTube API credentials
        credentials = Credentials.from_authorized_user_file(
            os.getenv("YOUTUBE_CREDENTIALS_PATH"), scopes=["https://www.googleapis.com/auth/youtube.readonly"]
        )
        youtube = build("youtube", "v3", credentials=credentials)

        # Fetch channel analytics data
        channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
        response = youtube.channels().list(
            part="statistics",
            id=channel_id
        ).execute()

        # Extract statistics
        stats = response["items"][0]["statistics"]
        youtube_data = [
            ("Subscribers", stats.get("subscriberCount", "N/A")),
            ("Total Views", stats.get("viewCount", "N/A")),
            ("Video Count", stats.get("videoCount", "N/A"))
        ]

        # Display data
        df_yt = pd.DataFrame(youtube_data, columns=["Metric", "Value"])
        st.dataframe(df_yt)
    except Exception as e:
        st.error(f"Error loading YouTube data: {e}")

st.caption("🔍 Replace YouTube placeholders with API data using the YouTube Analytics API (OAuth 2.0 required).")