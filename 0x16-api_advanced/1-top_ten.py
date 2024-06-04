#!/usr/bin/python3

"""Prints the first 10 hot title posts listed for a given subreddit"""

from requests import get


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    user = {'User-Agent': 'Rudzi'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
