"""
PYTHON LEVEL 4: MASTERY (AUTOMATION SPECIALIST)
===============================================
Topic: Framework Architecture & Scalability.

[THEORY]
1. Dynamic Frameworks: Loading classes by string name (Plugins).
2. Properties Management: Handling configs for multi-env.
3. CLI Tools: Building command-line interfaces.
4. Design Patterns: Singleton, Factory.
"""

import argparse
import importlib
import sys

# --- 1. Dynamic Class Loading (Plugin System) ---
class PluginManager:
    """
    Simulates a Test Runner that loads test classes dynamically based on name.
    """
    @staticmethod
    def load_plugin(module_name, class_name):
        try:
            # Dynamic import
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            return cls()
        except (ImportError, AttributeError) as e:
            print(f"Failed to load plugin: {e}")
            return None

# --- 2. Singleton Design Pattern (Configuration) ---
class ConfigSingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            cls._instance.settings = {"env": "PROD"} # Load once
            print("Config Loaded (First Time)")
        return cls._instance

# --- 3. CLI Tool Development Structure ---
# (This is typically in a separate main.py, but shown here for education)
def cli_demo():
    # In real usage: python mytool.py --env PROD
    parser = argparse.ArgumentParser(description="Automation CLI Tool")
    parser.add_argument("--env", help="Target Environment")
    
    # Simulating args for demo
    args = parser.parse_args(["--env", "QA"]) 
    print(f"CLI Argument Received: {args.env}")

# --- MINI PROJECT TASK ---
# Build a 'TestRunner' class that:
# 1. Scans a folder for .py files.
# 2. Looks for classes ending in 'Test'.
# 3. Instantiates and runs methods starting with 'test_'.
# (See portfolio/python-frameworks/main.py for a simplified version of this logic)

if __name__ == "__main__":
    print("--- Mastery Concepts ---")
    
    # Singleton Check
    c1 = ConfigSingleton()
    c2 = ConfigSingleton()
    print(f"Is c1 same object as c2? {c1 is c2}") # True
    
    # Plugin Demo (Mocking import of 'os' just to show reflection)
    # In real world, we would import 'tests.login_test'
    print("Dynamic Import Demo (Loading 'os.path'):")
    module = importlib.import_module("os")
    print(module.name)
    
    # CLI
    cli_demo()
