#!/usr/bin/python3
""" script to export data in the CSV format """

import json
import requests
import sys


def export_user_data(user_id):
    """
    get user data from api
    and export this data in the CSV format
    """
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{user_id}").json()
    user_todos = requests.get(f"{url}/users/{user_id}/todos").json()

    username = user.get('username')
    filename = user_id + '.json'

    with open(filename, "w") as json_file:
        json.dump({user_id: [{
        'task': t.get('title'),
        'completed': t.get('completed'),
        'username': username
        } for t in user_todos]}, json_file)


if __name__ == "__main__":
    export_user_data(sys.argv[1])
