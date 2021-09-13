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

    for user in req_user:
        taskList = []
        for task in req_todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
