tasks = []

def add_task(title: str) -> dict:
    """Creates a new task and adds it to the list."""
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    return task
