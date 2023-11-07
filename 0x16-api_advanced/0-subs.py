#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit,
             or 0 if the subreddit is invalid.
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'MyRedditClient/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()

    if "data" in data:
        return data.get("data").get("subscribers")
    else:
        return (0)
