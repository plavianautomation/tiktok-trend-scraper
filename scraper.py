import requests
import json

APIFY_TOKEN = "YOUR_APIFY_TOKEN"

url = f"https://api.apify.com/v2/acts/clockworks/tiktok-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"

payload = {
    "searchTerms": ["ai tools"],
    "resultsPerPage": 5
}

response = requests.post(url, json=payload)
data = response.json()

for video in data:
    print({
        "user": video.get("authorMeta", {}).get("name"),
        "likes": video.get("diggCount"),
        "url": video.get("webVideoUrl")
    })
