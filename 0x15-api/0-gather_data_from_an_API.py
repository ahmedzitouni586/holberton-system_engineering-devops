#!/usr/bin/python3
""" script that returns information about employees"""

import requests
import sys
if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    r = requests.get('https://jsonplaceholder.typicode.com/todos/{}'
                     .format(sys.argv[1]))
    jsondata = r.json()
    EMPLOYEE_NAME = jsondata.get("name")
    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                     format(sys.argv[1]))
    jsondata = r.json()
    for i in jsondata:
        if i.get("completed") is True:
            TASK_TITLE.append(i.get("title"))
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(jsondata)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS,
          TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print("\t {}".format(title))
