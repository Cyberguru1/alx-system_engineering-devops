#!/usr/bin/python3
"""returns information about his/her list progress """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{sys.argv[1]}").json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [h.get("title") for h in todos if h.get("completed") is True]
    
    print("Employee {} is done with tasks({}/{}:".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(h)) for h in completed]
