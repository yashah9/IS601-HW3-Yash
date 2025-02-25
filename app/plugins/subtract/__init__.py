"""Subtract Command Module

This module contains the implementation of the SubtractCommand class,
which performs subtraction of two decimal numbers.
"""

from decimal import Decimal, InvalidOperation
from app.commands import Command

class SubtractCommand(Command):
    """Command class to perform subtraction of two numbers."""

    def execute(self, *args):
        if len(args) != 2:
            return "Please provide exactly two numbers to subtract."

        try:
            a_decimal, b_decimal = map(Decimal, args)
            return f"The result of subtracting {b_decimal} from {a_decimal} is equal to {a_decimal - b_decimal}."
        except InvalidOperation:
            return f"Invalid number input: '{args[0]}' or '{args[1]}' is not a valid number."