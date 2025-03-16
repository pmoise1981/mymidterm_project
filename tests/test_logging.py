from calculator.logging_setup import setup_logging

def test_logging():
    logger = setup_logging()
    assert logger.level == 20  # INFO level

