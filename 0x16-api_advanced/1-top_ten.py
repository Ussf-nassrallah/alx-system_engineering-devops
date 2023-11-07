#!/usr/bin/python3
""" task-1 document """
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API
      and returns the first 10 hot posts listed
      for a given subreddit
    """
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}

    res = requests.get(
        apiUrl,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if res.status_code == 404:
        print('None')
        return
    output = res.json().get("data")
    for obj in output.get("children"):
        print(obj.get("data").get("title"))
