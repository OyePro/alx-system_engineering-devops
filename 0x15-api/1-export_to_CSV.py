#!/usr/bin/python3
"""A python script that exports data in csv format
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    userId = argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    username = user.json().get("username")

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos_list = []
    for todo in todos.json():
        if todo.get("userId") == int(userId):
            todos_list.append((todo.get('completed'), todo.get('title')))

    csv_file = f"{userId}.csv"
    csv_list = ['USER_ID', 'USERNAME', 'TASK_STATUS', 'TASK_TITLE']
    with open(csv_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=csv_list, quoting=csv.QUOTE_ALL)
        for task in todos_list:
            csv_rows = {'USER_ID': userId, 'USERNAME': username,
                        'TASK_STATUS': task[0], 'TASK_TITLE': task[1]}
            writer.writerow(csv_rows)
