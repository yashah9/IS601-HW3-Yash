from typing import List, Callable, Optional
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve all calculations."""
        return cls.history

    @classmethod
    def get_latest(cls) -> Calculation:
        """Retrieve the most recent calculation."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """Clear the history."""
        cls.history.clear()