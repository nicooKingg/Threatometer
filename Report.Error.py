import traceback
import requests
import sys
import os

# Configuration
GITHUB_TOKEN = "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"  # 🔐 Keep this secret
REPO_OWNER = "niccoKingg"
REPO_NAME = "Threatometer"
ISSUE_LABELS = ["bug", "auto-report"]

def create_github_issue(title, body):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    payload = {
        "title": title,
        "body": body,
        "labels": ISSUE_LABELS
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("✅ GitHub issue created successfully.")
    else:
        print(f"❌ Failed to create issue: {response.status_code} - {response.text}")

def main():
    try:
        # 👇 Put your actual code here
        x = 1 / 0  # Example error

    except Exception as e:
        error_type = type(e).__name__
        error_message = str(e)
        tb = traceback.format_exc()

        issue_title = f"Auto-Error Report: {error_type} - {error_message[:50]}"
        issue_body = f"""### 🐛 Error Report
**Error Type:** {error_type}  
**Error Message:** {error_message}

**Traceback:**
