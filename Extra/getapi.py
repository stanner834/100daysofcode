import requests

# Get all tasks
response = requests.get("http://127.0.0.1:5000/tasks")
print(response.json())

# Get a specific task by ID (replace `1` with the desired task ID)
response = requests.get("http://127.0.0.1:5000/tasks/1")
print(response.json())

# Create a new task
new_task = {"title": "New Task"}
response = requests.post("http://127.0.0.1:5000/tasks", json=new_task)
print(response.json())
