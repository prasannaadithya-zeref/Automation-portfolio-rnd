import sys
import os
import argparse
import pandas as pd
from datetime import datetime
from common.config_loader import ConfigLoader
from common.db_manager import DatabaseManager
from data_validation.comparator import DataComparator
from log_validation.parser import LogParser
from reporting.report_generator import ReportGenerator
from api_testing.api_tester import APITester

def parse_arguments():
    """Defines and parses command-line arguments (User Inputs)."""
    parser = argparse.ArgumentParser(description="Automation Portfolio Framework")
    parser.add_argument('--env', type=str, default='DEV', help='Target Environment (DEV, QA, PROD)')
    parser.add_argument('--run_api_tests', action='store_true', help='Flag to run API integration tests')
    parser.add_argument('--report_type', type=str, default='html', help='Report format (html/excel)')
    parser.add_argument('--report_dir', type=str, default='reports', help='Directory to save reports')
    return parser.parse_args()

def main():
    print("=========================================")
    print(" Automation Framework Portfolio Showcase ")
    print("=========================================")
    
    # 0. User Input Processing
    args = parse_arguments()
    print(f"[*] Arguments Received: {args}")
    
    # 1. Load Configuration
    config = ConfigLoader('config.properties')
    print(f"[*] Environment Locked To: {args.env}")
    
    # Initialize Modules
    db_manager = DatabaseManager(config)
    reporter = ReportGenerator(args.report_dir)
    validation_results = [] # Collect results for reporting

    # ---------------------------------------------------------
    # Scenario 1: Data Verification (Simulated Redshift vs Postgres)
    # ---------------------------------------------------------
    print("\n[*] Scenario: Multi-Database Verification")
    df_app = pd.DataFrame({'id': [101, 102, 103], 'amount': [50.0, 150.0, 200.0]})
    df_dwh = pd.DataFrame({'id': [101, 102, 103], 'amount': [50.0, 150.0, 201.0]}) # Intentionally diff
    
    match, diff = DataComparator.compare_dataframes(df_app, df_dwh, key_columns=['id'])
    
    if match:
        validation_results.append({'Test': 'DB Verification', 'Status': 'PASS', 'Message': 'Values match perfectly'})
    else:
        print("    [!] Mismatch found. Generating Excel failure report...")
        validation_results.append({'Test': 'DB Verification', 'Status': 'FAIL', 'Message': 'Discrepancy in amounts'})
        reporter.generate_excel_failure_report(diff, filename=f"failed_records_{args.env}.xlsx")

    # ---------------------------------------------------------
    # Scenario 2: API Integration Testing (Optional via CLI)
    # ---------------------------------------------------------
    if args.run_api_tests:
        print("\n[*] Scenario: API Health & Data Integrity")
        # In a real run, you'd start the mock server or hit a real URL
        # For demo, the base_url is dummy or mocked
        api = APITester("http://localhost:5000") 
        
        # Note: This will fail if the Mock API server isn't actually running in a separate terminal.
        # So we wrap it in a try/except for the portfolio demo to be safe.
        try:
            passed, _ = api.validate_get_status('health', 200)
            status = 'PASS' if passed else 'FAIL'
            validation_results.append({'Test': 'API Health Check', 'Status': status, 'Message': 'GET /health endpoint'})
        except Exception as e:
            print("    [!] API not reachable (Did you start api_mock/app.py?). Skipping...")
            validation_results.append({'Test': 'API Health Check', 'Status': 'SKIP', 'Message': 'Server unreachable'})

    # ---------------------------------------------------------
    # Final Reporting
    # ---------------------------------------------------------
    print("\n[*] Generating Execution Report...")
    run_meta = {
        'Environment': args.env,
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'User': os.getenv('USERNAME', 'User')
    }
    reporter.generate_html_report(run_meta, validation_results)
    print("=========================================")
    print(" Run Complete.")
    print("=========================================")

if __name__ == "__main__":
    main()
