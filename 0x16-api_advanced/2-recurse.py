#!/usr/bin/python3
"""Reddit client"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Querying Reddit API, and returns all
    hot articles for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'API Project by davixcky'}
    arg1 = {"limit": 100, "after": after}
    resp = requests.get(url, params=arg1, headers=headers)
    list_a = resp.json().get('data', {}).get('children', None)
    pagination = resp.json().get('data', {}).get('after', None)

    if pagination is not None:
        if list_a:
            for item in list_a:
                hot_list.append(item.get("data").get("title"))
        if pagination is not None:
            recurse(subreddit, hot_list, pagination)
        return hot_list
    else:
        return None
