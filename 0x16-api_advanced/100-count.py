#!/usr/bin/python3
"""Function to count words in all hot posts """
from itertools import count
import requests
from tempita import sub


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """prints counts of given words found in hot posts in a given subreddit
    Args:
        subreddit (str)
        word_list (list)
        instances (obj)
        after (str)
        count (int)
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for x in results.get("children"):
        title = x.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times
    if after is None:
        if len(instance) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda v: (-v[1], v[0]))
        [print(f"{k}: {v}" for k, v in instances)]
    else:
        count_words(subreddit, word_list, instances, after, count)
