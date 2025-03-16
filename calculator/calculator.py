import pandas as pd
import operator

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'result'])

    def add(self, a, b):
        try:
            result = a + b
            self._log_history('addition', result)
            return result
        except Exception as e:
            self._log_history('addition_error', str(e))
            raise ValueError(f"Error during addition: {e}")

    def subtract(self, a, b):
        try:
            result = a - b
            self._log_history('subtraction', result)
            return result
        except Exception as e:
            self._log_history('subtraction_error', str(e))
            raise ValueError(f"Error during subtraction: {e}")

    def multiply(self, a, b):
        try:
            result = a * b
            self._log_history('multiplication', result)
            return result
        except Exception as e:
            self._log_history('multiplication_error', str(e))
            raise ValueError(f"Error during multiplication: {e}")

    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
            self._log_history('division', result)
            return result
        except Exception as e:
            self._log_history('division_error', str(e))
            raise ValueError(f"Error during division: {e}")

    def _log_history(self, operation, result):
        success_entry = pd.DataFrame([[operation, result]], columns=['operation', 'result'])
        success_entry = success_entry.loc[:, success_entry.notna().any(axis=0)]
        self.history = pd.concat([self.history, success_entry], ignore_index=True)

    def get_history(self):
        return self.history

    # Updated evaluate method to raise the error without wrapping in ValueError
    def evaluate(self, expression):
        try:
            # Basic operator mapping for safe evaluation
            allowed_operators = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }

            # Split expression into operator and operands (very basic parser)
            for op, func in allowed_operators.items():
                if op in expression:
                    operands = expression.split(op)
                    if len(operands) == 2:
                        a, b = map(float, operands)

                        # Check for division by zero separately
                        if op == '/' and b == 0:
                            raise ZeroDivisionError("Cannot divide by zero")

                        result = func(a, b)
                        self._log_history(f"{a} {op} {b}", result)
                        return result
            raise ValueError("Invalid expression or unsupported operator")

        except ZeroDivisionError as e:
            self._log_history('evaluation_error', str(e))
            raise e  # Raising the ZeroDivisionError directly without wrapping it in ValueError
        except Exception as e:
            self._log_history('evaluation_error', str(e))
            raise ValueError(f"Error during evaluation: {e}")

