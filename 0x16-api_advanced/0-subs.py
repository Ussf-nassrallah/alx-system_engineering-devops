#!/usr/bin/python3
""" task-0 document """
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API
      and returns the number of subscribers
    """
    apiUrl = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(apiUrl, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    output = res.json().get("data")
    return output.get("subscribers")
