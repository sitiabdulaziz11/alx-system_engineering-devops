#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    respo = requests.get(url)
    users = respo.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('user_name')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        respo = requests.get(url)
        tasks = respo.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "user_name": user_name
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
