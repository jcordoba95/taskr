import pytest
from services.task_service import add_task, get_tasks
from services import storage
from unittest.mock import patch

@patch('services.task_service.storage.load_tasks')
@patch('services.task_service.storage.save_tasks')
def test_add_task(mock_save, mock_load):

    mock_load.return_value = []
    
    result = add_task("Buy bread")
    
    assert result["title"] == "Buy bread"
    assert "id" in result

    mock_save.assert_called_once()

@patch('services.task_service.storage.load_tasks')
def test_get_tasks_empty(mock_load):

    # Test believes JSON is empty
    mock_load.return_value = []

    # Should return an empty list if no tasks have been added yet
    tasks = get_tasks()
    assert len(tasks) == 0
