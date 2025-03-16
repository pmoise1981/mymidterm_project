import importlib

class PluginSystem:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin_name):
        module = importlib.import_module(plugin_name)
        self.plugins[plugin_name] = module

    def get_plugin(self, plugin_name):
        return self.plugins.get(plugin_name, None)

