#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress from a REST API and
displays it on the standard output. It accepts an employee ID as a parameter and formats the
output in a specific way.
Requirements for this script include using the 'requests' module and following the specified
output format.
"""
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
