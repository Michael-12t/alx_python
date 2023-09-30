import sys
import requests
import json

def export_to_json(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare JSON file name
    file_name = f"{employee_id}.json"

    # Prepare JSON data
    json_data = {str(employee_id): []}
    for task in todos_data:
        task_title = task['title']
        task_completed = task['completed']
        json_data[str(employee_id)].append({
            'task': task_title,
            'completed': task_completed,
            'username': employee_name
        })

    # Write JSON data to file
    with open(file_name, 'w') as file:
        json.dump(json_data, file)

    print(f"Data exported to {file_name}")

# Check if employee ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])
export_to_json(employee_id)