#!/usr/bin/python3
"""function that queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers for a given subreddit"""
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-agent": "custom"})
    if (r.status_code == 200):
        return r.json().get("data").get("subscribers")
    return 0
