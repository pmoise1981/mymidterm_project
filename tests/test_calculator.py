from calculator.calculator import Calculator

def test_calculator():
    calc = Calculator()
    assert calc.evaluate("2 + 3") == 5
    assert calc.evaluate("10 / 2") == 5.0
    assert calc.get_history().shape[0] == 2

