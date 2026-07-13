from datetime import datetime

tasks = []
task_counter = 1

def add_task(title: str) -> dict:
    """Creates a new task and adds it to the list."""
    global task_counter
    task = {
        "id": task_counter,
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "metadata": {}
    }
    tasks.append(task)
    task_counter += 1
    return task