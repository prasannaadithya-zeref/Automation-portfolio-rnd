"""
LEARNING LAB: Python OOP for Automation Engineers
=================================================
This file is designed to take you from a basic scripter to an OOP expert.
It demonstrates:
1. Classes & Objects
2. Constructor (__init__)
3. Inheritance (Parent -> Child)
4. Polymorphism (Overriding methods)
5. Encapsulation (Private variables)

Scenario: We are building a generic 'Connector' for different systems.
"""

from abc import ABC, abstractmethod

# 1. Abstract Base Class (Blueprints)
# -----------------------------------
# This enforces that all children MUST implement specific methods.
class GenericConnector(ABC):
    
    def __init__(self, name, timeout=30):
        self.name = name
        self.timeout = timeout
        # Encapsulation: _status is 'protected' (convention), __secret is 'private'
        self._status = "DISCONNECTED"
    
    @abstractmethod
    def connect(self):
        """Standard interface: All connectors must connect."""
        pass

    def get_status(self):
        return self._status

# 2. Inheritance & Polymorphism
# -----------------------------
class DatabaseConnector(GenericConnector):
    
    def __init__(self, db_type, host):
        # calling Parent's constructor
        super().__init__(name=f"{db_type}-Connector") 
        self.host = host

    # Overriding the abstract method
    def connect(self):
        print(f"[{self.name}] Connecting to DB at {self.host}...")
        self._status = "CONNECTED"

class APIConnector(GenericConnector):
    
    def __init__(self, url):
        super().__init__(name="REST-API")
        self.url = url

    def connect(self):
        print(f"[{self.name}] Handshaking with {self.url}...")
        self._status = "AUTHORIZED"

# 3. Usage (The 'Expert' part)
# ----------------------------
# Polymorphism in action: We can treat different objects the same way.
def system_check(connectors):
    print("\n--- System Health Check ---")
    for c in connectors:
        c.connect()  # Works for both DB and API objects!
        print(f"Status: {c.get_status()}")

if __name__ == "__main__":
    # creating instances
    db = DatabaseConnector("Postgres", "localhost:5432")
    api = APIConnector("https://api.example.com")
    
    # Passing them to a generic function
    system_check([db, api])
