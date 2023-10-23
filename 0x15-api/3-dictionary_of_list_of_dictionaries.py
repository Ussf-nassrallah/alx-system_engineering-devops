#!/usr/bin/python3
""" script to export data in the json format """

import json
import requests


def export_user_data():
    """
    get user data from api
    and export this data in the json format
    """
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users").json()
    todos = requests.get(f"{url}/todos").json()

    filename = 'todo_all_employees.json.json'

    with open(filename, "w") as json_file:
        json.dump({user.get('id'): [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('name')
        } for todo in todos] for user in users}, json_file)


if __name__ == "__main__":
    export_user_data()
