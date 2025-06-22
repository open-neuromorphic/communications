# community_engagement_streamlit.py

import os
import requests
from collections import Counter
import traceback
import streamlit as st

# Constants
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = os.getenv("DISCORD_GUILD_ID")
GETTING_INVOLVED_ROLE = "getting-involved"  # Role name to analyze

# Ensure required environment variables are set
if not DISCORD_BOT_TOKEN or not DISCORD_GUILD_ID:
    st.error("DISCORD_BOT_TOKEN and DISCORD_GUILD_ID must be set as environment variables.")
    st.stop()

HEADERS = {"Authorization": f"Bot {DISCORD_BOT_TOKEN}"}


def fetch_guild_roles(guild_id):
    url = f"https://discord.com/api/v10/guilds/{guild_id}/roles"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        st.error(f"Error {response.status_code}: {response.text}")
        traceback.print_exc()
        return []
    return response.json()


def fetch_all_members(guild_id):
    members = []
    after = None
    while True:
        params = {"limit": 1000}
        if after:
            params["after"] = after
        url = f"https://discord.com/api/v10/guilds/{guild_id}/members"
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            st.error(f"Error {response.status_code}: {response.text}")
            traceback.print_exc()
            return []
        batch = response.json()
        if not batch:
            break
        members.extend(batch)
        after = batch[-1]["user"]["id"]
    return members


def find_role_id(roles, role_name):
    for role in roles:
        if role["name"] == role_name:
            return role["id"]
    return None


def analyze_roles(members, role_id):
    total_members = len(members)
    role_counts = Counter()
    getting_involved_ids = []

    for member in members:
        roles = member.get("roles", [])
        role_counts.update(roles)
        if role_id in roles:
            getting_involved_ids.append(member["user"]["id"])

    getting_involved_count = len(getting_involved_ids)
    percent_involved = 100 * getting_involved_count / total_members if total_members > 0 else 0

    return role_counts, getting_involved_ids, getting_involved_count, percent_involved


def top_roles_for_users(members, user_ids, exclude_role_id, top_n=5):
    involved_roles = Counter()
    for member in members:
        if member["user"]["id"] in user_ids:
            involved_roles.update(member.get("roles", []))

    top_roles = involved_roles.most_common(top_n + 1)
    return [(r, c) for r, c in top_roles if r != exclude_role_id][:top_n]


def calculate_likelihoods(members, role_counts, getting_involved_ids, exclude_role_id):
    likelihoods = {}
    for role, _ in role_counts.items():
        with_role = [m["user"]["id"] for m in members if role in m.get("roles", [])]
        in_both = len(set(with_role) & set(getting_involved_ids))
        likelihood = 100 * in_both / len(with_role) if with_role else 0
        if role != exclude_role_id and len(with_role) > 10:
            likelihoods[role] = likelihood

    return sorted(likelihoods.items(), key=lambda x: x[1], reverse=True)[:10]


# Streamlit App
st.title("Community Engagement Dashboard")

roles = fetch_guild_roles(DISCORD_GUILD_ID)
GETTING_INVOLVED_ROLE_ID = find_role_id(roles, GETTING_INVOLVED_ROLE)

if not GETTING_INVOLVED_ROLE_ID:
    st.error(f"Role '{GETTING_INVOLVED_ROLE}' not found in the guild.")
    st.stop()

members = fetch_all_members(DISCORD_GUILD_ID)

role_counts, getting_involved_ids, getting_involved_count, percent_involved = analyze_roles(
    members, GETTING_INVOLVED_ROLE_ID
)

st.subheader(f"Users in '{GETTING_INVOLVED_ROLE}'")
st.write(f"Count: {getting_involved_count}")
st.write(f"Percent of Total Users: {percent_involved:.2f}%")

top_5_roles = top_roles_for_users(members, getting_involved_ids, GETTING_INVOLVED_ROLE_ID)
st.subheader(f"Top 5 Roles for '{GETTING_INVOLVED_ROLE}' Users")
for role, count in top_5_roles:
    st.write(f"{role}: {count} users")

likelihoods = calculate_likelihoods(members, role_counts, getting_involved_ids, GETTING_INVOLVED_ROLE_ID)
st.subheader(f"Likelihood of Being in '{GETTING_INVOLVED_ROLE}' by Role")
for role, pct in likelihoods:
    st.write(f"{role}: {pct:.2f}% likely also in '{GETTING_INVOLVED_ROLE}'")
