#!/usr/bin/python3
""" script to export data in the CSV format """

import csv
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
    filename = user_id + '.csv'

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
         ) for todo in user_todos]


if __name__ == "__main__":
    export_user_data(sys.argv[1])
