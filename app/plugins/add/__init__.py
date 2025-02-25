"""Add Command Module

This module contains the implementation of the AddCommand class,
which performs addition of two numbers.
"""

from decimal import Decimal, InvalidOperation
from app.commands import Command

class AddCommand(Command):
    """Command class to add two numbers."""

    def execute(self, *args):
        if len(args) != 2:
            return "Error: Please provide exactly two numbers to add."

        try:
            a_decimal, b_decimal = map(Decimal, args)
            return f"The result of adding {a_decimal} and {b_decimal} is equal to {a_decimal + b_decimal}."
        except InvalidOperation:
            return "Error: Invalid input. Please provide valid numbers."