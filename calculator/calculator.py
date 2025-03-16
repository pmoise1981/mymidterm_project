import logging
import pandas as pd

class Calculator:
    def __init__(self):
        # Initialize history DataFrame
        self.history = pd.DataFrame(columns=["expression", "result"])

        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info("Calculator initialized.")

    def evaluate(self, expression):
        try:
            result = eval(expression)
            self.history = pd.concat(
                [self.history, pd.DataFrame([{"expression": expression, "result": result}])],
                ignore_index=True
            )
            logging.info(f"Evaluated expression: {expression} = {result}")
            return result
        except Exception as e:
            logging.error(f"Error evaluating expression: {expression}. Error: {e}")
            return f"Error: {e}"

    def get_history(self):
        logging.info("History retrieved.")
        return self.history

