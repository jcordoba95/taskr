import pytest
from services.task_service import add_task, tasks
import services.task_service as task_service

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # This runs before every test to guarantee isolation!
    tasks.clear()
    task_service.task_counter = 1
    yield

def test_add_task():
    task = add_task("Buy groceries")
    assert task["id"] == 1
    assert task["title"] == "Buy groceries"
    assert task["completed"] is False
    assert "created_at" in task
    assert "metadata" in task
    assert len(tasks) == 1
