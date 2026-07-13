import os
import pytest
import services.task_service as task_service

# Use a separate test file so we don't mess up real tasks!
TEST_FILE = "test_tasks.json"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Before test: point the service to our test file
    task_service.TASKS_FILE = TEST_FILE

    # Make sure we start with a clean slate
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    yield # This runs the actual test

    # After test: clean up the test file
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_task():
    task = task_service.add_task("Buy groceries")
    assert task["title"] == "Buy groceries"
    assert task["completed"] is False

    # Verify it was saved and can be retrieved
    tasks = task_service.get_tasks()
    assert len(tasks) == 1
    assert tasks[0] == task

def test_get_tasks_empty():
    # Should return an empty list if no tasks have been added yet
    tasks = task_service.get_tasks()
    assert len(tasks) == 0
