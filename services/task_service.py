from datetime import datetime
from services import storage

def add_task(title: str) -> dict:
    """Creates a new task and adds it to the list."""
    tasks = storage.load_tasks()

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
    storage.save_tasks(tasks)
    return task

def get_tasks() -> list:
    """Returns the list of all tasks."""
    return storage.load_tasks()