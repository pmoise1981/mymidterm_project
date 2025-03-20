import pytest
from calculator import Calculator

def test_calculator():
    calc = Calculator()

    # Test valid expression
    result = calc.calculate("2 + 3")
    assert result == 5

    # Test zero division
    with pytest.raises(ZeroDivisionError):
        calc.calculate("1 / 0")
    
    # Test invalid syntax (empty expression)
    with pytest.raises(ValueError):
        calc.calculate("")
    
    # Test invalid syntax (incomplete expression)
    with pytest.raises(ValueError):
        calc.calculate("2 +")

    # Test unsupported operator
    with pytest.raises(ValueError):
        calc.calculate("2 @ 3")
    
    # Test large number multiplication
    result = calc.calculate("1000000 * 1000000")
    assert result == 1e12

    # Test exponentiation
    result = calc.calculate("2 ** 3")
    assert result == 8

    # Test history logging
    calc.calculate("2 + 3")
    history = calc.get_history()
    assert len(history) == 1
    assert history['expression'][0] == "2 + 3"
    assert history['result'][0] == 5

