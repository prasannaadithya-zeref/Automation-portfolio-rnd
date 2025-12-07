import os

class ConfigLoader:
    """
    A unified Configuration Loader that supports .properties files.
    Demonstrates ability to handle environment-specific configurations.
    """
    def __init__(self, config_path):
        self.config_path = config_path
        self.properties = {}
        self._load_properties()

    def _load_properties(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    self.properties[key.strip()] = value.strip()

    def get(self, key, default=None):
        return self.properties.get(key, default)

    def get_as_int(self, key, default=0):
        val = self.get(key)
        return int(val) if val else default

    def get_as_boolean(self, key, default=False):
        val = self.get(key)
        if val:
            return val.lower() in ('true', 'yes', '1', 'on')
        return default
