#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    function that prints the titles of the first 10 hot posts.
    """

    url = 'https://www.reddit.com'
    api_uri = '{main}/r/{subrdt}/hot.json'.format(main=url, subrdt=subreddit)

    user_agent = {'User-Agent': 'Python/requests'}
    restrict = {'limit': '10'}

    result = requests.get(api_uri, headers=user_agent,
                          params=restrict,
                          allow_redirects=False)

    if result.status_code in [302, 404]:
        print('None')
    else:
        json_result = result.json()

        if json_result.get('data') and json_result.get('data').get('children'):
            top_post = json_result.get('data').get('children')

            for i in top_post:
                if i.get('data') and i.get('data').get('title'):
                    print(i.get('data').get('title'))
