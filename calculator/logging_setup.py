import logging

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Explicitly set to INFO
    if not logger.hasHandlers():  # Avoid duplicate handlers
        handler = logging.StreamHandler()  # For console output
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)

        # File handler to log to a file
        file_handler = logging.FileHandler('app.log')  # Logs will be written to app.log
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)

    return logger

# If you want to run the script directly (for example, testing):
if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Logging setup complete")

