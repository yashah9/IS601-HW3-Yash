"""Divide Command Module

This module contains the implementation of the DivideCommand class,
which performs division of two numbers.
"""

from decimal import Decimal, InvalidOperation
from app.commands import Command

class DivideCommand(Command):
    """Command class to divide two numbers."""

    def execute(self, *args):
        if len(args) != 2:
            return "Please provide exactly two numbers to divide."

        try:
            a_decimal, b_decimal = map(Decimal, args)
            if b_decimal == 0:
                return "Error: Division by zero is not allowed."
            return f"The result of dividing {a_decimal} by {b_decimal} is equal to {a_decimal / b_decimal}."
        except InvalidOperation:
            return f"Invalid number input: '{args[0]}' or '{args[1]}' is not a valid number."