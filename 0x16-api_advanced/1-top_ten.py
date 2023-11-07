#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditClient/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])

    for post in data:
        title = post.get('data', {}).get('title', '')
        print(title)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass a subreddit name as an argument.")
    else:
        top_ten(sys.argv[1])
