import sys
import requests
import csv

def export_to_csv(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare CSV file name
    file_name = f"{employee_id}.csv"

    # Prepare CSV data
    csv_data = []
    for task in todos_data:
        task_id = task['id']
        task_title = task['title']
        task_completed = task['completed']
        csv_data.append([employee_id, employee_name, str(task_completed), task_title])

    # Write CSV data to file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f"Data exported to {file_name}")

# Check if employee ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 export_to_CSV.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])
export_to_csv(employee_id)