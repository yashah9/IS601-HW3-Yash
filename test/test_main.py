# pylint: disable=missing-docstring, invalid-name, unnecessary-dunder-call
import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    pytest.param("20", "4", 'divide', "The result of 20 divide 4 is equal to 5",
                 marks=pytest.mark.skip(reason="Division tests are skipped")),
    pytest.param("1", "0", 'divide', "Cannot divide by zero",
                 marks=pytest.mark.skip(reason="Division tests are skipped")),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    # You can add more cases for invalid inputs here if needed.
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string