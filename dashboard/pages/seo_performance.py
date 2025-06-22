
# seo_performance.py

import streamlit as st
import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import date, timedelta

st.set_page_config(page_title="SEO Performance", layout="wide")
st.title("🔎 SEO Performance (Search Console)")

# Config
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
PROPERTY_URI = os.getenv("GSC_PROPERTY_URI")  # e.g., 'https://yourdomain.com/'

def load_gsc_data(credentials_json, site_url):
    credentials = service_account.Credentials.from_service_account_file(
        credentials_json, scopes=SCOPES
    )
    service = build("searchconsole", "v1", credentials=credentials)

    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    request = {
        "startDate": str(start_date),
        "endDate": str(end_date),
        "dimensions": ["query"],
        "rowLimit": 10
    }

    response = (
        service.searchanalytics()
        .query(siteUrl=site_url, body=request)
        .execute()
    )

    rows = response.get("rows", [])
    data = [
        {
            "Query": row["keys"][0],
            "Clicks": row.get("clicks", 0),
            "Impressions": row.get("impressions", 0),
            "CTR (%)": round(row.get("ctr", 0) * 100, 2),
            "Position": round(row.get("position", 0), 2),
        }
        for row in rows
    ]
    return pd.DataFrame(data)

try:
    # Load data from GSC
    credentials_path = os.getenv("GSC_SERVICE_ACCOUNT_PATH")  # Path to service account key
    df = load_gsc_data(credentials_path, PROPERTY_URI)

    st.subheader("🔍 Top Queries (Last 30 Days)")
    st.dataframe(df)

    st.subheader("📊 Summary Stats")
    total_clicks = int(df["Clicks"].sum())
    total_impressions = int(df["Impressions"].sum())
    avg_ctr = round(df["CTR (%)"].mean(), 2)
    avg_position = round(df["Position"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Clicks", f"{total_clicks:,}")
    col2.metric("Total Impressions", f"{total_impressions:,}")
    col3.metric("Avg. CTR", f"{avg_ctr}%")
    col4.metric("Avg. Position", f"{avg_position}")

except Exception as e:
    st.error(f"Error loading Search Console data: {e}")
