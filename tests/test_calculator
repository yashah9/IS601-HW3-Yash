'''test_calculator.py'''
import os
import pytest
import pandas as pd
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand


@pytest.fixture
def add_command():
    """Create an instance of the AddCommand class for testing."""
    return AddCommand()


@pytest.fixture
def subtract_command():
    """Create an instance of the SubtractCommand class for testing."""
    return SubtractCommand()


@pytest.fixture
def multiply_command():
    """Create an instance of the MultiplyCommand class for testing."""
    return MultiplyCommand()

@pytest.fixture
def divide_command():
    """Create an instance of the DivideCommand class for testing."""
    return DivideCommand()
#add command
def test_add_command(add_command):
    """Test the add command."""
    result = add_command.execute(3, 5)
    assert result == "The result of adding 3 and 5 is equal to 8."

def test_add_invalid_input(add_command):
    """Test the add command with invalid input (non-numeric)."""
    result = add_command.execute("a", 5)
    assert result == "Error: Invalid input. Please provide valid numbers."

    result = add_command.execute(3, "b")
    assert result == "Error: Invalid input. Please provide valid numbers."

    result = add_command.execute("x", "y")
    assert result == "Error: Invalid input. Please provide valid numbers."

def test_add_insufficient_arguments(add_command):
    """Test the add command with insufficient number of arguments."""
    result = add_command.execute(3)
    assert result == "Error: Please provide exactly two numbers to add."

    result = add_command.execute()
    assert result == "Error: Please provide exactly two numbers to add."

def test_add_too_many_arguments(add_command):
    """Test the add command with more than two arguments."""
    result = add_command.execute(3, 5, 7)
    assert result == "Error: Please provide exactly two numbers to add."

# subtract command
def test_subtract_command(subtract_command):
    """Test the subtract command."""
    result = subtract_command.execute(5, 3)
    assert result == "The result of subtracting 3 from 5 is equal to 2."

def test_subtract_command_invalid_input(subtract_command):
    """Test the subtract command with invalid input (non-numeric)."""
    result = subtract_command.execute("a", 5)
    assert result == "Invalid number input: 'a' or '5' is not a valid number."

    result = subtract_command.execute(3, "b")
    assert result == "Invalid number input: '3' or 'b' is not a valid number."

    result = subtract_command.execute("x", "y")
    assert result == "Invalid number input: 'x' or 'y' is not a valid number."

def test_subtract_insufficient_arguments(subtract_command):
    """Test the subtract command with insufficient number of arguments."""
    result = subtract_command.execute(5)
    assert result == "Please provide exactly two numbers to subtract."

    result = subtract_command.execute()
    assert result == "Please provide exactly two numbers to subtract."

def test_subtract_too_many_arguments(subtract_command):
    """Test the subtract command with more than two arguments."""
    result = subtract_command.execute(5, 3, 2)
    assert result == "Please provide exactly two numbers to subtract."

# multiply command
def test_multiply_command(multiply_command):
    """Test the multiply command."""
    result = multiply_command.execute(3, 5)
    assert result == "The result of multiplying 3 and 5 is equal to 15."

def test_multiply_invalid_input(multiply_command):
    """Test the multiply command with invalid input (non-numeric)."""
    result = multiply_command.execute("a", 5)
    assert result == "Invalid number input: 'a' or '5' is not a valid number."

    result = multiply_command.execute(3, "b")
    assert result == "Invalid number input: '3' or 'b' is not a valid number."

    result = multiply_command.execute("x", "y")
    assert result == "Invalid number input: 'x' or 'y' is not a valid number."

def test_multiply_insufficient_arguments(multiply_command):
    """Test the multiply command with insufficient number of arguments."""
    result = multiply_command.execute(3)
    assert result == "Please provide exactly two numbers to multiply."

    result = multiply_command.execute()
    assert result == "Please provide exactly two numbers to multiply."

def test_multiply_too_many_arguments(multiply_command):
    """Test the multiply command with more than two arguments."""
    result = multiply_command.execute(3, 5, 7)
    assert result == "Please provide exactly two numbers to multiply."

# divide command
def test_divide_command(divide_command):
    """Test the divide command."""
    result = divide_command.execute(10, 2)
    assert result == "The result of dividing 10 by 2 is equal to 5."
    # Test division by zero
    result_zero_division = divide_command.execute(5, 0)
    assert result_zero_division == "Error: Division by zero is not allowed."

def test_divide_negative_numbers(divide_command):
    """Test the divide command with negative numbers."""
    result = divide_command.execute(-10, 2)
    assert result == "The result of dividing -10 by 2 is equal to -5."

    result = divide_command.execute(10, -2)
    assert result == "The result of dividing 10 by -2 is equal to -5."

    result = divide_command.execute(-10, -2)
    assert result == "The result of dividing -10 by -2 is equal to 5."

def test_divide_invalid_input(divide_command):
    """Test the divide command with invalid input (non-numeric)."""
    result = divide_command.execute("a", 5)
    assert result == "Invalid number input: 'a' or '5' is not a valid number."

    result = divide_command.execute(3, "b")
    assert result == "Invalid number input: '3' or 'b' is not a valid number."

    result = divide_command.execute("x", "y")
    assert result == "Invalid number input: 'x' or 'y' is not a valid number."

def test_divide_insufficient_arguments(divide_command):
    """Test the divide command with insufficient number of arguments."""
    result = divide_command.execute(3)
    assert result == "Please provide exactly two numbers to divide."

    result = divide_command.execute()
    assert result == "Please provide exactly two numbers to divide."

def test_divide_too_many_arguments(divide_command):
    """Test the divide command with more than two arguments."""
    result = divide_command.execute(3, 5, 7)
    assert result == "Please provide exactly two numbers to divide."

def test_divide_by_zero(divide_command):
    """Test the divide command where the divisor is zero."""
    result = divide_command.execute(5, 0)
    assert result == "Error: Division by zero is not allowed."
