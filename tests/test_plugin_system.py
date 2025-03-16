import pytest
from calculator.plugin_system import PluginSystem

def test_plugin_system():
    plugin_system = PluginSystem()
    assert plugin_system is not None
