import sys
import requests

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Count number of completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

# Check if employee ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])
get_employee_todo_progress(employee_id)