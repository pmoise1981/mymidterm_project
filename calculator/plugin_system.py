import logging_setup

def example_plugin_function():
    logger = logging_setup.setup_logging()
    logger.info("Plugin system initialized.")
    logger.warning("This is a warning from the plugin system.")
    logger.error("This is an error from the plugin system.")

def main():
    example_plugin_function()  # Call the function inside main()

if __name__ == "__main__":
    main()  # Ensure main() is executed when running the script

