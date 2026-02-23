#!/usr/bin/python3
"""
Query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced.project:v1.0 (by /u/reddit_api)"
    }
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    children = response.json().get("data", {}).get("children", [])

    if not children:
        print(None)
        return

    for post in children:
        print(post.get("data").get("title"))
