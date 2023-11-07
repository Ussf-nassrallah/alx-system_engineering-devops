#!/usr/bin/python3
""" task-2 document """
import requests


def recurse(subreddit, hot_list=[], af="", counter=0):
    """
    function that queries the Reddit API
    and returns a list containing the titles of
    all hot articles for a given subreddit
    """
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 100, "count": counter, "after": af}

    res = requests.get(
        apiUrl,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if res.status_code == 404:
        return

    output = res.json().get("data")
    af = output.get("after")
    counter += output.get("dist")

    for obj in output.get("children"):
        hot_list.append(obj.get("data").get("title"))

    if af is not None:
        return recurse(subreddit, hot_list, af, counter)
    return hot_list
