#!/usr/bin/python3
"""
 Python script that export data in the CSV format.
 """

import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    request = requests.get(url_user)

    user_name = request.json().get('username')
    task = url_user + '/todos'
    request = requests.get(task)
    tasks = request.json()

    with open('{}.csv'.format(user), 'w') as csv_file:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
