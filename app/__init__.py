import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
import os
import sys
import logging
import logging.config
import pandas as pd
# from dotenv import load_dotenv
# from tabulate import tabulate
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.hello import HelloCommand
from app.plugins.greet import GreetCommand
"""
Main application module for executing basic mathematical commands.

This module initializes the application, configures logging,
and registers basic arithmetic commands.
"""



class App:
    """Main application class to manage command execution."""

    def __init__(self):
        """Initialize the application and configure logging."""
        self.command_handler = CommandHandler()
        self.register_commands()

    def register_commands(self):
        """Register arithmetic command classes with the command handler."""
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("hello", HelloCommand())
        self.command_handler.register_command("greet", GreetCommand())

        # Debugging: Print registered commands
        logging.info(f"Registered commands: {list(self.command_handler.commands.keys())}")

    def handle_command_input(self, cmd_input):
        """Handle the execution of commands based on user input."""
        parts = cmd_input.strip().split()
        if not parts:
            print("No command entered.")
            return

        command = parts[0]
        args = parts[1:]

        if command in self.command_handler.commands:
            try:
                result = self.command_handler.execute_command(command, *args)
                print(result)
            except Exception as e:
                # logging.error("Error executing command: %s", e)
                print(f"Error: {e}")
        else:
            # logging.error("Unknown command: %s", command)
            print(f"No such command: {command}")

    def start(self):
        """Start the REPL for command input."""
        self.display_menu()
        # logging.info("Application started.")

        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == "exit":
                    print("Exiting...")
                    # logging.info("Application exit.")
                    sys.exit()

                self.handle_command_input(cmd_input)

        except KeyboardInterrupt:
            # logging.info("Application interrupted and exiting gracefully.")
            print("\nExiting...")
            sys.exit()

    def display_menu(self):
        """Display available commands."""
        print("\nAvailable Commands:")
        print("1. add       - Add numbers (e.g., add 3 4)")
        print("2. subtract  - Subtract numbers (e.g., subtract 10 5)")
        print("3. multiply  - Multiply numbers (e.g., multiply 2 3)")
        print("4. divide    - Divide numbers (e.g., divide 8 2)")
        print("5. hello     - Responds with 'Hello, World!'")
        print("6. greet     - Greets a user (e.g., greet Alice)")
        print("\nType 'exit' to quit the application.\n")
    
    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
 

if __name__ == "__main__":
    app = App()
    app.start()