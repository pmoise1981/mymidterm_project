import logging

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Explicitly set to INFO
    if not logger.hasHandlers():  # Avoid duplicate handlers
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)
    return logger

