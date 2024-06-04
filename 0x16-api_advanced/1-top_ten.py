#!/usr/bin/python3
'''
This module contains the function top_ten.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
    Fetches and prints the top ten posts for a given subreddit.
    '''
    headers = {'User-Agent': 'Reddit-Top-Ten-Script/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors

        data = response.json()

        # Extract and print the titles of the top ten posts
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Reddit API: {e}")
        print(None)
    except (KeyError, TypeError) as e:
        print(f"Error parsing response data: {e}")
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./script_name.py <subreddit>")
