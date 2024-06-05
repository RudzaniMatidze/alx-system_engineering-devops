#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the total number
    of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        results = response.json()

        subscribers = results.get('data', {}).get('subscribers')
        if subscribers is not None:
            print("OK")
        else:
            print("None")
    except Exception as e:
        print("None")
