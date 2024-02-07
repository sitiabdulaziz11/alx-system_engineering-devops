#!/usr/bin/python3
"""
Python script that export TODO data in the JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    emply_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + emply_id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {emply_id: []}
    for task in tasks:
        dictionary[emply_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(emply_id), 'w') as filename:
        json.dump(dictionary, filename)
