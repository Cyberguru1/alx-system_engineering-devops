#!/usr/bin/python3
"""
Using what you did in the task #0, extend your 
Python script to export data in the CSV format.
"""
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{user_id}").json()
    username = user.get("username")
    print(username)
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    
    with open(f"{user_id}.csv", "w", newline="") as f:
        cursor = csv.writer(f, quoting=csv.QUOTE_ALL)
        [cursor.writerow(
            [user_id, username, h.get("completed"), h.get("title")]
        ) for h in todos]
