#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """

import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json{}".format(subreddit, after)
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0',
                            allow_redirects=False})

    if response.status_code != 404:
        dict_obj = response.json()
        list_obj = dict_obj.get('data').get('children')
        for each in list_obj:
            hot_list.append(each.get('data').get('title'))
        next_fullname = dict_obj.get('data').get('after')
        after = "?after={}".format(next_fullname)

        if next_fullname is not None:
            hot_list.append(recurse(subreddit, hot_list, after))

        return hot_list
    else:
        return None
