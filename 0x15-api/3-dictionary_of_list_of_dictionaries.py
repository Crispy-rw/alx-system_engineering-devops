#!/usr/bin/python3
"""
Using a REST API, for a given employee ID and returns information
about his/her TODO list progress.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    req_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    req_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    with open('todo_all_employees.json', mode='w') as json_file:

        jsonfile = {}

        for i in req_user:
            USER_ID = i.get('id')
            jsonfile[USER_ID] = []

            for j in req_todos:
                if USER_ID == j.get('userId'):
                    USERNAME = i.get('username')
                    TASK_COMPLETED_S = j.get('completed')
                    TASK_TITLE = j.get('title')

                    jsonfile[USER_ID].append({'task': TASK_TITLE,
                                              'completed': TASK_COMPLETED_S,
                                              'username': USERNAME})

        json.dump(jsonfile, json_file)
