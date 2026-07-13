import json
import os
from datetime import datetime

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
    
    # Figure out the next ID based on existing tasks
    next_id = max((t.get("id", 0) for t in tasks), default=0) + 1
    
    task = {
        "id": next_id,
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "metadata": {}
    }
    tasks.append(task)
    _save_tasks(tasks)
    return task

def get_tasks() -> list:
    """Returns the list of all tasks."""
    return _load_tasks()