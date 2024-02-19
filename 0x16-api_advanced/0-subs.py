#!/usr/bin/python3
"""
module that queries the Reddit API and returns the number of subscribe.
"""

import requests


def number_of_subscribers(subreddit):
    """function that returns the number of subscribers for
    a given subreddit.
    """

    url = 'https://www.reddit.com'
    api_url = '{main}/r/{subrdt}/about.json'.format(main=url, subrdt=subreddit)
    user_agent = {'User-Agent': 'Python/requests'}

    result = requests.get(api_url, headers=user_agent, allow_redirects=False)
    if result.status_code in [302, 404]:
        return 0
    return result.json().get('data').get('subscribers')
