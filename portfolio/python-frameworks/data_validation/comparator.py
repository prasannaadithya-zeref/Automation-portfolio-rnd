import pandas as pd
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataComparator:
    """
    Core data validation engine.
    Capable of comparing:
    1. Two Pandas DataFrames (simulating DB vs Excel)
    2. JSON Object vs Expected Schema/Values
    """

    @staticmethod
    def compare_dataframes(df_source, df_target, key_columns):
        """
        Compares two dataframes based on key columns.
        Returns: Tuple (match_status: bool, differences: DataFrame)
        """
        logger.info(f"Starting DataFrame comparison on keys: {key_columns}")
        
        # Ensure keys exist
        for col in key_columns:
            if col not in df_source.columns or col not in df_target.columns:
                raise ValueError(f"Key column {col} missing in one of the datasets.")

        # Merge to find discrepancies
        # using indicator=True to find presence in both
        merged = pd.merge(df_source, df_target, on=key_columns, how='outer', indicator=True, suffixes=('_src', '_tgt'))
        
        diffs = merged[merged['_merge'] != 'both']
        
        if diffs.empty:
            logger.info("DataFrames match perfectly.")
            return True, None
        else:
            logger.info(f"Found {len(diffs)} mismatches.")
            return False, diffs

    @staticmethod
    def validate_json(actual_json, expected_schema_rules):
        """
        Validates a JSON object against dynamic rules.
        expected_schema_rules: dict of 'field_path': 'expected_value' or 'type'
        """
        logger.info("Starting JSON validation...")
        errors = []
        
        for field, rule in expected_schema_rules.items():
            # Simple navigation for nested keys "attr.sub_attr"
            keys = field.split('.')
            value = actual_json
            try:
                for k in keys:
                    value = value.get(k)
            except AttributeError:
                value = None # Path doesn't exist

            # Validation Logic
            if isinstance(rule, dict) and 'type' in rule:
                 if type(value).__name__ != rule['type']:
                     errors.append(f"Type Mismatch for {field}: Expected {rule['type']}, Got {type(value).__name__}")
            elif value != rule:
                errors.append(f"Value Mismatch for {field}: Expected {rule}, Got {value}")

        if not errors:
            logger.info("JSON validation passed.")
            return True, []
        else:
            logger.error(f"JSON validation failed with {len(errors)} errors.")
            return False, errors
