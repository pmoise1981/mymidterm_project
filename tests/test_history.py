import pytest
from calculator.calculator import Calculator

def test_history_after_error():
    calc = Calculator()  # Fresh instance

    # Valid case, should succeed
    calc.evaluate("10 / 2")

    # Error case, expecting ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        calc.evaluate("10 / 0")

    # Check if history was updated correctly, including the error
    history = calc.get_history()
    assert len(history) == 2  # History should contain both operations
    assert "evaluation_error" in history['operation'].iloc[-1]  # Ensure error is logged


