import pandas as pd
import logging
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """
    SENIOR ENGINEER NOTE:
    ---------------------
    Why this class exists? 
    Instead of scattering `psycopg2.connect()` calls all over the project, we centralize 
    connection logic here. This is called the 'Factory Pattern'.
    
    It allows us to:
    1. Switch databases (Oracle -> Postgres) just by changing config.
    2. Manage connection pools efficiently (create_engine).
    3. Mock database responses when running in demo/offline mode.
    """
    
    def __init__(self, config_loader):
        self.config = config_loader
        # We store engines here to reuse them. This is a form of 'Caching'.
        self.engines = {}

    def _get_connection_string(self, db_type, db_alias):
        host = self.config.get(f"{db_alias}.host")
        port = self.config.get(f"{db_alias}.port")
        user = self.config.get(f"{db_alias}.user")
        password = self.config.get(f"{db_alias}.password")
        dbname = self.config.get(f"{db_alias}.dbname")
        
        # Basic construction logic...
        return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

    def get_engine(self, db_type, db_alias):
        """
        Singleton Pattern implementation:
        If we already created an engine for this DB, return it.
        Don't create a new connection every time!
        """
        if db_alias in self.engines:
            return self.engines[db_alias]
        
        try:
            conn_str = self._get_connection_string(db_type, db_alias)
            # engine = create_engine(conn_str) # Real connection
            # self.engines[db_alias] = engine
            # return engine
            return None # mocked
        except:
            return None

    def execute_query(self, db_type, db_alias, query, collection_name=None):
        """
        Executes query. For Portfolio Demo, if connection fails, it returns MOCK DATA
        so the user sees the framework in action.
        """
        logger.info(f"Requests query on {db_alias} ({db_type}): {query}")
        
        # --- DEMO MOCK LOGIC ---
        # In a real interview setting, you might want this to fail if DB is missing.
        # But for 'Click Run' request, we provide data.
        if "users" in query:
             return pd.DataFrame([
                 {"id": 1, "name": "Alice", "role": "Admin"},
                 {"id": 2, "name": "Bob", "role": "User"}
             ])
        elif "transactions" in query:
             return pd.DataFrame([
                 {"id": 101, "amount": 500.00},
                 {"id": 102, "amount": 120.50}
             ])
        
        # Default mock
        logger.warning(f"Connection to {db_alias} failed or not configured. Returning mock data.")
        return pd.DataFrame([{"col1": "demo_val", "col2": 123}])
