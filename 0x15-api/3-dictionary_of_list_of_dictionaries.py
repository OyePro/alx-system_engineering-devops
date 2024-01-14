#!/usr/bin/python3
"""A python script that exports data in json format
"""
import json
import requests

if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    ids = []
    for user in users.json():
        ids.append(user.get('id'))

    users_dict = {}
    for i_d in ids:
        for user in users.json():
            if user.get('id') == i_d:
                username = user.get('username')
        http = f'https://jsonplaceholder.typicode.com/todos?userId={i_d}'
        todos = requests.get(f'{http}')
        todos_list = []
        for todo in todos.json():
            todos_list.append((todo.get('completed'), todo.get('title')))

        task_list = []
        for task in todos_list:
            task_dict = {'username': username, 'task': task[1],
                         'completed': task[0]}
            task_list.append(task_dict)
        users_dict[i_d] = task_list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json.dump(users_dict, f)
