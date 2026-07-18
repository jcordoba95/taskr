from datetime import datetime
from services import storage
import uuid

def add_task(title: str) -> dict:
    """Creates a new task and adds it to the list."""
    tasks = storage.load_tasks()
    task = {
        "id": str(uuid.uuid4()),
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "metadata": {}
    }
    tasks.append(task)
    storage.save_tasks(tasks)
    return task

def get_tasks() -> list:
    """Returns the list of all tasks."""
    return storage.load_tasks()
