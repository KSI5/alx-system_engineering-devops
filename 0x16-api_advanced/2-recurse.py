#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = f"https://api.reddit.com/r/{subreddit}?sort=hot&limit=100&after={after}"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (None)

    response = response.json()
    data = response.get("data", {})

    if not data.get("children"):
        return (hot_list)

    for post in data["children"]:
        hot_list.append(post["data"]["title"])

    next_page = data.get("after")

    if next_page:
        return recurse(subreddit, hot_list, next_page)

    return (hot_list)
