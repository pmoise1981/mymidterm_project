# My Midterm Calculator Project

## Overview

This project is a Python-based calculator with advanced features like history management, plugin support, and professional logging. It includes a command-line interface (REPL), dynamic plugin loading, and a history management system that uses pandas. The project is built with an emphasis on modularity, logging, and automated testing.

## Features

### 1. [Calculator Class](#calculator-class)
   The `Calculator` class evaluates mathematical expressions and performs basic arithmetic operations such as add, subtract, multiply, and divide. It is designed to be extensible with new functionalities through plugins.

### 2. [History Manager](#history-manager)
   A robust history manager powered by [Pandas](https://pandas.pydata.org/) to store calculation histories in a CSV file. Users can view, load, and clear previous calculations through the REPL interface.

### 3. [Plugin System](#plugin-system)
   The plugin system allows dynamic loading of new commands and features without modifying the core code. New plugins can be integrated to extend the calculator’s functionalities seamlessly.

### 4. [Logging](#logging)
   Comprehensive logging is implemented using Python’s `logging` module. The system logs errors, operations, and informational messages, and the logging level can be configured dynamically using environment variables.

### 5. [Test Coverage](#test-coverage)
   The project ensures 100% test coverage using [pytest](https://pytest.org/) for all modules and features. Tests are automated to run with GitHub Actions whenever changes are pushed.

---

## Design Patterns Used

### 1. **Facade Pattern**
   The **Facade Pattern** simplifies interactions with the complex Pandas operations. It hides the intricacies of Pandas' DataFrame manipulations and provides a simple interface for managing the calculation history. 

   - **Link**: [Facade Pattern Implementation](./calculator/facade.py)

### 2. **Command Pattern**
   The **Command Pattern** is used to encapsulate the REPL commands (such as add, subtract, and load history) as objects. This design allows commands to be executed, undone, or re-executed in a clean and decoupled manner.

   - **Link**: [Command Pattern Implementation](./calculator/command.py)

### 3. **Factory Method Pattern**
   The **Factory Method Pattern** is used to create different types of commands dynamically. It abstracts object creation, ensuring that new commands can be added without modifying the core application.

   - **Link**: [Factory Method Pattern Implementation](./calculator/factory.py)

### 4. **Singleton Pattern**
   The **Singleton Pattern** is applied to the logging system, ensuring only one instance of the logger is used throughout the entire application. This pattern helps maintain consistency in logging and ensures that all log messages are routed to the same destination.

   - **Link**: [Singleton Pattern Implementation](./calculator/singleton.py)

### 5. **Strategy Pattern**
   The **Strategy Pattern** is used in the plugin system to switch between different calculation strategies or methods dynamically, without changing the core algorithm of the calculator.

   - **Link**: [Strategy Pattern Implementation](./calculator/strategy.py)

---

## Environment Variables

Environment variables are used for dynamic configuration of the logging system, allowing different logging levels (e.g., DEBUG, INFO, WARNING, ERROR) and output destinations (e.g., console or log file). The configuration of the logging system can be adjusted by simply modifying environment variables without altering the core code.

### Example of environment variable usage:

```python
import os
import logging

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
i
