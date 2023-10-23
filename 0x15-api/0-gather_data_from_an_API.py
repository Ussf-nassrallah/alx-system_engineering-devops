#!/usr/bin/python3
"""
script that, using 'https://jsonplaceholder.typicode.com' REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com"
user_id = sys.argv[1]


def get_user_data(user_id):
    user = requests.get(f"{url}/users/{user_id}")
    user_todos = requests.get(f"{url}/users/{user_id}/todos")

    NUMBER_OF_DONE_TASKS = 0
    EMPLOYEE_NAME = user.json().get('name')
    TOTAL_NUMBER_OF_TASKS = len(user_todos.json())
    DONE_TASKS = []

    for todo in user_todos.json():
        if todo.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            DONE_TASKS.append(todo)

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS
    ))

    for task in DONE_TASKS:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    get_user_data(user_id)