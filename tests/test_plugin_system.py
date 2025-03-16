from calculator.plugin_system import PluginSystem

def test_plugin():
    ps = PluginSystem()
    ps.load_plugin("math")
    assert "math" in ps.plugins

