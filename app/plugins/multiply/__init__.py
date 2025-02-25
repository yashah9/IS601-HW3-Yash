"""Multiply Command Module

This module contains the implementation of the MultiplyCommand class,
which performs multiplication of two given numbers.
"""

from decimal import Decimal, InvalidOperation
from app.commands import Command

class MultiplyCommand(Command):
    """Command class to multiply two numbers."""

    def execute(self, *args):
        if len(args) != 2:
            return "Please provide exactly two numbers to multiply."

        try:
            a_decimal, b_decimal = map(Decimal, args)
            return f"The result of multiplying {a_decimal} and {b_decimal} is equal to {a_decimal * b_decimal}."
        except InvalidOperation:
            return f"Invalid number input: '{args[0]}' or '{args[1]}' is not a valid number."