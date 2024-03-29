#!/usr/bin/python3
"""
 REST API, for a given employee ID, returns information
 about TODO list progress.
"""

import requests
import sys


if __name__ == '__main__':
    emply_Id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + emply_Id

    response = requests.get(url)
    employeeName = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
