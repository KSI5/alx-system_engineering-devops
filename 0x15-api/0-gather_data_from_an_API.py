#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress from a REST API and
displays it on the standard output. It accepts an employee ID as a parameter and formats the
output in a specific way.
Requirements for this script include using the 'requests' module and following the specified
output format.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url, params={"userId": employee_id})
        todos_data = todos_response.json()

        # Calculate progress
        completed_tasks = [todo["title"] for todo in todos_data if todo["completed"]]
        total_tasks = len(todos_data)

        # Display progress
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except (KeyError, IndexError):
        print("Error: Employee not found or invalid response data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
