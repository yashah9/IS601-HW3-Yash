'''Test_App.py'''
from unittest.mock import MagicMock
import pytest
from app import App, CommandHandler

@pytest.fixture
def app():
    """Create an instance of the App class for testing."""
    return App()

@pytest.fixture
def command_handler():
    """Create an instance of the CommandHandler class for testing."""
    return CommandHandler()

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_command_handler_register_command(command_handler):
    """Test command registration."""
    mock_command = MagicMock()

    command_handler.register_command("mock", mock_command)
    assert "mock" in command_handler.commands
    assert command_handler.commands["mock"] == mock_command

def test_command_handler_execute_command_valid(command_handler):
    """Test executing a valid command."""
    mock_command = MagicMock()
    mock_command.execute.return_value = "Executed"

    command_handler.register_command("mock", mock_command)
    result = command_handler.execute_command("mock")

    assert result == "Executed"
    mock_command.execute.assert_called_once()