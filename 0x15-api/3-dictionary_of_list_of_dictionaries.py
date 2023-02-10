#!/usr/bin/python3
"""
Using what you did in the task #0, extend your 
Python script to exports to-do list information 
of all employees to JSON format.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            h.get("id") : [{
                "task": hh.get("title"),
                "completed": hh.get("completed"),
                "username": hh.get("username"),
            } for hh in requests.get(url + "todos", 
                                    params = {"userId": h.get("id")}).json()]
        for h in user}, f)
