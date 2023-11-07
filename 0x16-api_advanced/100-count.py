#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively count keywords in hot articles on a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str, optional): The Reddit API 'after' parameter for pagination.
        counts (dict, optional): Dictionary to store keyword counts.

    Returns:
        None
    """
    if counts is None:
        counts = {}
    
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyRedditClient/1.0'}

    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    response.raise_for_status()

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            keyword = word.lower()
            if keyword in title:
                if keyword in counts:
                    counts[keyword] += 1
                else:
                    counts[keyword] = 1

    after = data.get('data', {}).get('after')
    
    if after and len(posts) > 0:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: python3 script.py subreddit keyword1 keyword2 ...")
    else:
        subreddit_name = sys.argv[1]
        keywords = sys.argv[2:]
        count_words(subreddit_name, keywords)
