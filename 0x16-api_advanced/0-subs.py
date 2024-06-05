#!/usr/bin/python3
"""How many subs"""

import requests


def number_of_subscribers(subreddit):
    """reddit api that returns no of sub"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(sunreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
