from services.task_service import add_task, tasks

def test_add_task():
    # Clear the global tasks list before the test (to ensure isolation)
    tasks.clear()

    # Run the function
    task = add_task("Buy groceries")

    # Assertions
    assert task["title"] == "Buy groceries"
    assert task["completed"] is False
    assert len(tasks) == 1
    assert tasks[0] == task
