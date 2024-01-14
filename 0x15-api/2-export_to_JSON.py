#!/usr/bin/python3
"""A python script that exports data in csv format
"""
import requests
from sys import argv
import json

if __name__ == "__main__":

    userId = argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    username = user.json().get("username")

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos_list = []
    for todo in todos.json():
        if todo.get("userId") == int(userId):
            todos_list.append((todo.get('completed'), todo.get('title')))

    filename = f"{userId}.json"
    task_list = []
    for task in todos_list:
        task_dict = {'task': task[1], 'completed': task[0],
                     'username': username}
        task_list.append(task_dict)
    json_form = {userId: task_list}
    with open(filename, 'w') as f:
        json.dump(json_form, f)
