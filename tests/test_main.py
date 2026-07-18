import argparse
from unittest.mock import patch
from main import handle_command

@patch('main.add_task') # Mock import
def test_handle_command_add(mock_add_task):
    # Simulate the user entry "python main.py add 'Buy milk'"
    args = argparse.Namespace(command="add", title="Buy milk")

    # Call dispatcher
    handle_command(args)

    # Verify dispatcher trying to call add_task correctly
    mock_add_task.assert_called_once_with("Buy milk")
