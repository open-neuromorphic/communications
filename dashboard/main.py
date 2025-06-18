import streamlit as st

st.set_page_config(page_title="Open Neuromorphic Dashboard", layout="centered")
st.title("🧠 Open Neuromorphic Engagement Dashboard")
st.markdown("Welcome! Use the links below to explore different engagement metrics across ONM's platforms.")

st.divider()

st.subheader("🔍 Navigation")

st.page_link("pages/overall_health_growth.py", label="📊 Overall Health & Growth")
# st.page_link("website_metrics.py", label="🌐 Website Performance & Engagement")
# st.page_link("seo_performance.py", label="🔎 SEO Performance")
# st.page_link("content_hub.py", label="📝 Content Hub (Blog, Workshops, YouTube)")
# st.page_link("community_engagement.py", label="🤝 Community Engagement (Discord, LinkedIn)")

st.divider()

st.caption("📈 This dashboard is a work-in-progress. Data is updated via APIs from Google Analytics, Search Console, YouTube, Discord, and LinkedIn.")