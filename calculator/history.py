import pandas as pd
import logging_setup

class History:
    def __init__(self):
        self.logger = logging_setup.setup_logging()
        self.history = pd.DataFrame(columns=["Expression", "Result", "Status"])

    def add_entry(self, expression, result, status="Success"):
        new_entry = pd.DataFrame([{"Expression": expression, "Result": result, "Status": status}])
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.logger.info(f"Added to history: {expression} = {result} ({status})")

    def show_history(self):
        print(self.history)

def main():
    history = History()
    history.add_entry("2 + 3", 5)
    history.add_entry("10 / 0", "Error", status="Failed")
    history.show_history()

if __name__ == "__main__":
    main()

