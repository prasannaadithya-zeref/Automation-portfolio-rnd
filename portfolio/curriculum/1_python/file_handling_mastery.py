"""
FILE HANDLING MASTERY
=====================
As an Automation Engineer, you deal with Data.
This module covers reading/writing every common format:
1. TXT (Logs)
2. CSV (Data Driven Testing)
3. JSON (API Responses)
4. YAML (Configuration)
5. XML (Legacy/SOAP)
6. Excel (Business Data)
"""

import csv
import json
import xml.etree.ElementTree as ET
import sys

# Try importing non-standard libs (handling user env issues)
try:
    import pandas as pd
    import yaml # pip install pyyaml
except ImportError:
    print("Warning: Pandas or PyYAML not installed. install with: pip install pandas pyyaml")

class FileProcessor:
    
    # 1. TEXT FILES (Log Parsing)
    @staticmethod
    def read_text(filepath):
        print(f"\n--- READING TEXT: {filepath} ---")
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                print(f"Content Sample: {content[:50]}...")
        except FileNotFoundError:
            print("File not found.")

    # 2. CSV FILES (The bread and butter)
    @staticmethod
    def read_csv_native(filepath):
        print("\n--- READING CSV (Native) ---")
        data_list = []
        with open(filepath, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)
        return data_list

    @staticmethod
    def read_csv_pandas(filepath):
        """Pro Tip: Use Pandas for huge CSVs"""
        print("\n--- READING CSV (Pandas) ---")
        try:
            df = pd.read_csv(filepath)
            print(df.head())
        except NameError:
            print("Pandas not installed.")

    # 3. JSON FILES (Config / API)
    @staticmethod
    def read_json_safe(filepath):
        print("\n--- READING JSON ---")
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data

    # 4. XML FILES (Older Reporting)
    @staticmethod
    def read_xml(filepath):
        print("\n--- READING XML ---")
        tree = ET.parse(filepath)
        root = tree.getroot()
        for child in root:
            print(f"Tag: {child.tag}, Attributes: {child.attrib}")

    # 5. YAML (Modern Config)
    @staticmethod
    def read_yaml(filepath):
        print("\n--- READING YAML ---")
        try:
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
            return data
        except NameError:
            print("PyYAML not installed.")

def create_dummy_files():
    """Creates dummy files so this script actually runs."""
    with open("test.txt", "w") as f: f.write("Error: System Fail\nInfo: Startup Success")
    with open("data.csv", "w") as f: f.write("id,name\n1,Alice\n2,Bob")
    with open("config.json", "w") as f: f.write('{"url": "google.com", "retries": 3}')
    with open("data.xml", "w") as f: f.write('<users><user id="1">Alice</user></users>')

if __name__ == "__main__":
    create_dummy_files()
    
    processor = FileProcessor()
    processor.read_text("test.txt")
    print("CSV Data:", processor.read_csv_native("data.csv"))
    print("JSON Data:", processor.read_json_safe("config.json"))
    processor.read_xml("data.xml")
