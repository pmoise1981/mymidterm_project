import pandas as pd

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=["expression", "result"])

    def evaluate(self, expression):
        try:
            result = eval(expression)
            self.history = pd.concat(
                [self.history, pd.DataFrame([{"expression": expression, "result": result}])]
            )
            return result
        except Exception as e:
            return f"Error: {e}"

    def get_history(self):
        return self.history

