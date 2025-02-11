"""Unit tests for the Calculations history class."""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add

@pytest.fixture
def setup_calculations():
    """Fixture to clear the history and add two calculations for testing."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal("10"), Decimal("5"), add))
    Calculations.add_calculation(Calculation(Decimal("20"), Decimal("3"), add))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal("3"), Decimal("2"), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test that the history contains the expected number of calculations."""
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test that clearing the history results in an empty history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest(setup_calculations):
    """Test that retrieving the latest calculation returns the correct calculation."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal("20") and latest.b == Decimal("3"), "Did not get the correct latest calculation"

def test_get_latest_with_empty_history():
    """Test that retrieving the latest calculation from an empty history returns None."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
