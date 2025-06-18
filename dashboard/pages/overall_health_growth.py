# overall_health_growth.py

import streamlit as st
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest
from google.auth import default


import requests
import os
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Optional: for formatting large numbers
def format_number(n):
    return f"{n:,}"

st.set_page_config(page_title="Overall Health & Growth", layout="wide")
st.title("📊 Overall Health & Growth")

# ----------------------------------------
# SECTION 1: Google Analytics - Website Users
# ----------------------------------------
with st.expander("🌐 Website Users (GA4)", expanded=True):
    try:
        SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
        KEY_PATH = Path("~", ".config/gcloud/application_default_credentials.json").expanduser()

        # credentials = service_account.Credentials.from_service_account_file(
        #     KEY_PATH, scopes=SCOPES
        # )
        credentials, project_id = default(scopes=["https://www.googleapis.com/auth/analytics.readonly"])

        # Initialize the Google Analytics client
        client = BetaAnalyticsDataClient(credentials=credentials)

        # Replace with your Google Analytics property ID
        property_id = os.getenv("GA4_PROPERTY_ID")

        # Define the request for new users
        new_users_request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[],
            metrics=[{"name": "newUsers"}],
            date_ranges=[{"start_date": "30daysAgo", "end_date": "today"}],
        )

        # Fetch the report for new users
        new_users_response = client.run_report(new_users_request)

        # Extract the new users from the response
        new_users = int(new_users_response.rows[0].metric_values[0].value)

        # Define the request for total users
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[],
            metrics=[{"name": "activeUsers"}],
            date_ranges=[{"start_date": "30daysAgo", "end_date": "today"}],
        )

        # Fetch the report
        response = client.run_report(request)

        # Extract the total users from the response
        total_users = int(response.rows[0].metric_values[0].value)

        col1, col2 = st.columns(2)
        col1.metric("Total Website Users", format_number(total_users))
        col2.metric("New Website Users", format_number(new_users))
    except Exception as e:
        st.error(f"Error loading GA4 metrics: {e}")

# ----------------------------------------
# SECTION 2: Discord - Member Count
# ----------------------------------------
with st.expander("💬 Discord Members"):
    try:
        DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
        DISCORD_GUILD_ID = os.getenv("DISCORD_GUILD_ID")
        # Placeholder: Replace with Discord API logic or cached summary file
        headers = {
            "Authorization": f"Bot {DISCORD_BOT_TOKEN}"
        }
        url = f"https://discord.com/api/v10/guilds/{DISCORD_GUILD_ID}?with_counts=true"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        member_count = data["approximate_member_count"]

        st.metric("Total Discord Members", format_number(member_count))
        discord_members = 1987  # Replace with API or txt extract

        st.metric("Total Discord Members", format_number(discord_members))
    except Exception as e:
        st.error(f"Error loading Discord data: {e}")

# ----------------------------------------
# SECTION 3: YouTube - Subscribers
# ----------------------------------------
with st.expander("📺 YouTube Subscribers"):
    try:
        # Placeholder: Replace with YouTube Analytics API logic
        # Initialize the YouTube API client
        YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

        # Fetch the channel statistics
        channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
        response = youtube.channels().list(
            part="statistics",
            id=channel_id
        ).execute()

        # Extract the subscriber count
        yt_subscribers = int(response["items"][0]["statistics"]["subscriberCount"])
        # yt_subscribers = 354  # Replace with API call result

        st.metric("YouTube Subscribers", format_number(yt_subscribers))
    except Exception as e:
        st.error(f"Error loading YouTube data: {e}")

# ----------------------------------------
# SECTION 4: LinkedIn - Followers
# ----------------------------------------
with st.expander("💼 LinkedIn Followers"):
    try:
        # Placeholder: Replace with LinkedIn API or text file extract
        linkedin_followers = 642  # Replace with API call result

        st.metric("LinkedIn Followers", format_number(linkedin_followers))
    except Exception as e:
        st.error(f"Error loading LinkedIn data: {e}")

# ----------------------------------------
# Notes
# ----------------------------------------
st.caption("⚙️ Note: All values above are placeholders and should be replaced with real API calls or loaded data.")