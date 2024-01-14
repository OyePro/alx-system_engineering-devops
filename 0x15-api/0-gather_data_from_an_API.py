#!/usr/bin/python3
"""A python script that returns information of an employee in a given REST API
"""
import requests
from sys import argv

if __name__ == "__main__":

    userId = argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    employee_name = user.json().get("name")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo = todos.json()
    todos_list = []
    for dicts in todo:
        if dicts.get("userId") == eval(userId):
            todos_list.append(dicts)

    total_tasks = len(todos_list)
    done_tasks = []
    for task in todos_list:
        if task.get("completed") is True:
            done_tasks.append(task["title"])
    no_done_tasks = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          no_done_tasks,
                                                          total_tasks))
    for tasks in done_tasks:
        print(f"\t {tasks}")
