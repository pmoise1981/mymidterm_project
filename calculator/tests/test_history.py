from calculator.calculator import Calculator
import pytest

def test_addition():
    calc = Calculator()
    result = calc.evaluate("2 + 3")
    assert result == 5

def test_subtraction():
    calc = Calculator()
    result = calc.evaluate("10 - 5")
    assert result == 5

def test_multiplication():
    calc = Calculator()
    result = calc.evaluate("4 * 3")
    assert result == 12

def test_division():
    calc = Calculator()
    result = calc.evaluate("10 / 2")
    assert result == 5.0

def test_float_operations():
    calc = Calculator()
    result = calc.evaluate("2.5 + 3.5")
    assert result == 6.0
    result = calc.evaluate("5.5 - 2.5")
    assert result == 3.0

def test_invalid_expression():
    calc = Calculator()
    result = calc.evaluate("10 / 0")
    assert result == "Error: division by zero"

def test_invalid_syntax():
    calc = Calculator()
    result = calc.evaluate("2 +")
    assert result == "Error: unexpected EOF while parsing"

def test_large_number():
    calc = Calculator()
    result = calc.evaluate("1000000000 * 1000000")
    assert result == 1e12  # Large number check

def test_get_history():
    calc = Calculator()
    calc.evaluate("2 + 3")
    calc.evaluate("5 * 5")
    history = calc.get_history()
    assert len(history) == 2
    assert history.iloc[0]['expression'] == "2 + 3"
    assert history.iloc[1]['expression'] == "5 * 5"
    assert history.iloc[0]['result'] == 5
    assert history.iloc[1]['result'] == 25

def test_get_empty_history():
    calc = Calculator()
    history = calc.get_history()
    assert history.empty  # History should be empty initially

def test_exponential():
    calc = Calculator()
    result = calc.evaluate("2 ** 3")
    assert result == 8

def test_history_after_error():
    calc = Calculator()
    calc.evaluate("10 / 2")
    calc.evaluate("10 / 0")  # Error
    history = calc.get_history()
    assert len(history) == 3
    assert history.iloc[2]['expression'] == "10 / 0"
    assert history.iloc[2]['result'] == "Error: division by zero"

