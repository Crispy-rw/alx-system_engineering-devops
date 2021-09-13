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

    id_user = int(sys.argv[1])

    req_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    req_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    j_file = sys.argv[1] + '.json'

    with open(j_file, mode='w') as json_file:

        jsonfile = {}

        for i in req_user:
            if id_user == i.get('id'):
                USERNAME = i.get('username')

        lists = []

        for j in req_todos:
            TASK_COMPLETED_STATUS = j.get('completed')
            TASK_TITLE = j.get('title')
            if id_user == j.get('userId'):
                lists.append({'task': TASK_TITLE,
                              'completed': TASK_COMPLETED_STATUS,
                              'username': USERNAME})
                jsonfile = {id_user: lists}

        json.dump(jsonfile, json_file)
