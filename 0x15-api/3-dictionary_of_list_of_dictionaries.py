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

    filename = 'todo_all_employees.json'

    with open(filename, "w") as json_file:
        json.dump({u.get('id'): [{
            'username': u.get('username'),
            'task': t.get('title'),
            'completed': t.get('completed')
        }
            for t in requests.get(f"{url}/users/{u.get('id')}/todos").json()]
                for u in users}, json_file)


if __name__ == "__main__":
    export_user_data()
