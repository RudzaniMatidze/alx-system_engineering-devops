#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""

from requests import get, exceptions


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the total number
    of subscribers for a given subreddit. If the subreddit is invalid,
    returns 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        results = response.json()
        subscribers = results.get('data', {}).get('subscribers', 0)
        return subscribers
    except (exceptions.HTTPError, exceptions.RequestException, ValueError, KeyError):
        return 0
