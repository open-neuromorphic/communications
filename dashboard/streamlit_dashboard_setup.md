Here’s the cleaned-up and unified version of your full setup instructions in raw Markdown. Redundant steps were merged, order clarified, and formatting tightened:

# 🧠 Open Neuromorphic Engagement Dashboard

This dashboard tracks engagement across ONM’s platforms (Website, Discord, YouTube, LinkedIn) using data from Google Analytics 4 (GA4), Google Search Console, and other APIs.

---

## 🚀 Getting Started

Follow these steps to set up and run the Streamlit dashboard locally.

---

## 1. 🧰 Prerequisites

Ensure the following are installed:

- Python 3.9 or higher
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
- [Streamlit](https://streamlit.io)
- Required Python packages (see below)

---


## 2. 📁 Clone the Repository

```bash
git clone https://github.com/your-org/onm-engagement-dashboard.git
cd onm-engagement-dashboard
```

---


3. 🐍 Set Up Python Environment

Using venv:

python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

pip install -r requirements.txt


⸻

## 4. 🔐 GA4 API Authentication (for overall_health_growth.py)

To run overall_health_growth.py, set up Google Analytics API access using Application Default Credentials (ADC):

Step 1: Initialize Google Cloud CLI

If you haven’t already:

gcloud init

Step 2: Authenticate with Google and Set Scopes

gcloud auth application-default login \
  --scopes="https://www.googleapis.com/auth/analytics.readonly"

This allows your Python scripts to access GA4 as your Google user.

Step 3: Set a Quota Project

gcloud auth application-default set-quota-project YOUR_PROJECT_ID

Replace YOUR_PROJECT_ID with your Google Cloud project ID.

Step 4: Enable the GA4 Data API

gcloud services enable analyticsdata.googleapis.com --project=YOUR_PROJECT_ID

Step 5: Ensure GA4 Property Access

Go to analytics.google.com → Admin → Property Access Management.

Add your Google account (used in gcloud login) as a Viewer or Analyst.

⸻

## 5. ⚙️ Project Structure

Your project directory should look like this:

/dashboard/
│
├── home.py
├── overall_health_growth.py
├── website_metrics.py
├── seo_performance.py
├── content_hub.py
├── community_engagement.py
├── test_ga4_connection.py
├── requirements.txt
└── .streamlit/
    └── config.toml

Edit .streamlit/config.toml to customize sidebar or page titles if desired.

⸻

## 6. ▶️ Run the Dashboard

From the repo root:

streamlit run home.py

Then open http://localhost:8501 in your browser.

⸻

## 7. 📊 Dashboard Pages

## 7. 📊 Dashboard Pages

| Page                  | Description                                           |
|-----------------------|-------------------------------------------------------|
| **Home**              | Main navigation page                                  |
| **Overall Health & Growth** | Users, Discord members, YouTube subs, LinkedIn stats |
| **Website Metrics**   | GA4: traffic, top pages, engagement metrics           |
| **SEO Performance**   | Search Console: queries, impressions, CTR             |
| **Content Hub**       | Blog, workshops, and YouTube content performance      |
| **Community Engagement** | Discord role stats and LinkedIn follower insights   |


⸻

## ❓ Troubleshooting
	•	PERMISSION_DENIED: Ensure you’ve set the quota project and have GA4 access.
	•	Missing token_uri or client_email: You may be using the wrong credentials file. Use gcloud auth application-default login or create a valid service account JSON.

⸻

## 🔐 Notes
	•	This dashboard uses Application Default Credentials (ADC) for local development.
	•	For production use, a service account is recommended with securely stored credentials.

⸻

## 📬 Contact

Questions? Reach out in the ONM Discord or submit a pull request to contribute.