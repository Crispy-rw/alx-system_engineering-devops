#!/usr/bin/python3
"""
Using a REST API, for a given employee ID and returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":

    id_user = int(sys.argv[1])
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    req_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    req_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    print('Employee ', end='')

    for i in req_user:
        if id_user == i.get('id'):
            EMPLOYEE_NAME = i.get('name')

    for j in req_todos:
        total_task = j.get('userId')
        if total_task == id_user:
            TOTAL_NUMBER_OF_TASKS += 1

            number_task = j.get('completed')
            if number_task is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(j.get('title'))

    print('{} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for j in TASK_TITLE:
        print('\t {}'.format(j))
