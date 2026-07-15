import pytest
from services.task_service import add_task, get_tasks
from services import storage

@pytest.fixture(autouse=True)
def setup_and_teardown(tmp_path, monkeypatch):
    # Create a fake file path inside the guaranteed-empty temporary folder
    fake_file = tmp_path / "test_tasks.json"
    
    # Swap out the real TASKS_FILE variable in storage.py with our fake one
    monkeypatch.setattr(storage, "TASKS_FILE", str(fake_file))

    # We don't need a cleanup step anymore, Pytest deletes tmp_path automatically

def test_add_task():
    task = add_task("Buy groceries")
    assert task["id"] == 1
    assert task["title"] == "Buy groceries"
    assert task["completed"] is False
    assert "created_at" in task
    assert "metadata" in task

    # Verify it was saved and can be retrieved
    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0] == task

def test_get_tasks_empty():
    # Should return an empty list if no tasks have been added yet
    tasks = get_tasks()
    assert len(tasks) == 0