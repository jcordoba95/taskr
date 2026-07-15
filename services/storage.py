import json 
import os

TASKS_FILE = "tasks.json"

def load_tasks() -> list:
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks: list):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    