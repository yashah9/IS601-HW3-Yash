"""Command and CommandHandler class

This module defines the Command abstract base class and the CommandHandler class,
which manages command registration and execution.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self):
        """Execute the command."""

class CommandHandler:
    """Class to manage command registration and execution."""

    def __init__(self):
        """Initialize the CommandHandler with an empty command registry."""
        self.commands = {}

    def register_command(self, name, command):
        """Register a command with a given name.

        Args:
            name (str): The name of the command.
            command (Command): The command instance to register.
        """
        self.commands[name] = command

    def execute_command(self, command_name, *args):
        """Execute a command by name, passing any arguments to it.

        Args:
            command_name (str): The name of the command to execute.
            *args: Arguments to pass to the command's execute method.

        Raises:
            KeyError: If the command does not exist.
        """
        command = self.commands.get(command_name)
        if command is not None:
            return command.execute(*args)  # Pass the args to the command's execute method
        raise KeyError(f"No such command: {command_name}")