#import logging_setup
from calculator.logging_setup import setup_logging 

def example_plugin_function():
    logger = setup_logging()  # ✅ Direct function call
    logger.info("Plugin system initialized.")
    logger.warning("This is a warning from the plugin system.")
    logger.error("This is an error from the plugin system.")

def main():
    example_plugin_function()

if __name__ == "__main__":
    main()

