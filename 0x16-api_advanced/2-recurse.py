#!/usr/bin/python3
""" task-2 document """
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
    function that queries the Reddit API
      and returns a list containing the titles of
      all hot articles for a given subreddit
    """
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10, "count": count, "after": after}

    res = requests.get(
        apiUrl,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if res.status_code == 404:
        return

    output = res.json().get("data")
    after = output.get("after")
    count += output.get("dist")

    for obj in output.get("children"):
        hot_list.append(obj.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
