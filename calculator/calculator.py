import operator
import pandas as pd
import logging

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=["expression", "result"])
        # Updated allowed operators to include exponentiation
        self.allowed_operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow  # Exponentiation
        }
        logging.basicConfig(level=logging.INFO)

    def _log_history(self, expression, result):
        """Logs the expression and result into history"""
        self.history = self.history.append({
            'expression': expression,
            'result': result
        }, ignore_index=True)

    def calculate(self, expression):
        """Evaluates the mathematical expression"""
        try:
            # Basic validation for empty or invalid expressions
            if not expression:
                raise ValueError("Empty expression")
            
            # Split expression by space for basic parsing (could be extended for more complex cases)
            tokens = expression.split()
            if len(tokens) < 3:
                raise ValueError("Incomplete expression")

            operand1 = float(tokens[0])
            operator = tokens[1]
            operand2 = float(tokens[2])

            if operator not in self.allowed_operators:
                raise ValueError(f"Unsupported operator: {operator}")
            
            result = self.allowed_operators[operator](operand1, operand2)

            # Log to history
            self._log_history(expression, result)

            return result
        except ZeroDivisionError:
            logging.error("Division by zero is not allowed.")
            raise ZeroDivisionError("Cannot divide by zero")
        except ValueError as e:
            logging.error(f"Invalid expression: {e}")
            raise ValueError(f"Invalid expression: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise Exception(f"An error occurred: {e}")

    def get_history(self):
        """Returns the history of calculations"""
        return self.history

