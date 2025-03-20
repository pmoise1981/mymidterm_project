import pytest
from calculator.plugin_system import example_plugin_function

def test_plugin_system():
    assert example_plugin_function() is None  # Ensure it runs without errors

