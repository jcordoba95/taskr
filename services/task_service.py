import json
import os

TASKS_FILE = "tasks.json"

def _load_tasks() -> list:
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def _save_tasks(tasks: list):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title: str) -> dict:
    """Creates a new task and adds it to the list."""
    tasks = _load_tasks()
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    _save_tasks(tasks)
    return task

def get_tasks() -> list:
    """Returns the list of all tasks."""
    return _load_tasks()
