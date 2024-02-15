#!/usr/bin/python3
"""
Module that use recursive function and queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests
next_val = None


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit AP
    """
    global next_val
    user_agent = {'User-Agent': 'api_advanced-project'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    param = {'next_val': next_val}
    response = requests.get(url, params=param, headers=user_agent,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    response_data = response.json().get('data').get('next_val')
    if response_data is not None:
        next_val = response_data
        recurse(sudreddit, hot_list)

    titles = response.json().get('data').get("children")
    for i in titles:
        hot_list.append(i.get("data").get('title'))
    return hot_list
