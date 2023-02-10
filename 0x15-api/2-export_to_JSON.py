#!/usr/bin/python3
""" Python script to export data in the json format."""
import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{user_id}").json()
    username = user.get("username")
    print(username)
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
            "task": h.get("title"),
            "completed": h.get("completed"),
            "username": h.get("usernam")
        } for h in todos]}, f)
