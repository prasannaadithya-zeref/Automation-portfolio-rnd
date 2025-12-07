"""
GenAI LOG ANALYZER
==================
Demonstrating "Vibe Coding" & LLM Integration in Automation.

Problem: CI/CD logs are 50MB text files. Finding the ROOT CAUSE takes 20 mins.
Solution: Send the error stacktrace to an LLM to get a "One Line Summary".

Dependencies: `pip install openai` (Mocked here for portable portfolio)
"""

import os
import json

class GenAILogAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        # In real life: self.client = OpenAI(api_key=api_key)

    def extract_error_block(self, log_path):
        """Standard Logic: Read huge file, find 'ERROR' block."""
        error_lines = []
        capture = False
        with open(log_path, 'r') as f:
            for line in f:
                if "CRITICAL FAILURE" in line:
                    capture = True
                if capture:
                    error_lines.append(line)
                    if len(error_lines) > 20: break # Context window limit
        return "".join(error_lines)

    def analyze_with_llm(self, error_text):
        """
        PROMPT ENGINEERING:
        We don't just ask "What is this?".
        We use 'Role Prompting' and 'Output Constraints'.
        """
        system_prompt = "You are a Senior DevOps Engineer. Analyze this stacktrace."
        user_prompt = f"""
        Here is a crash log:
        {error_text}

        Task:
        1. Identify the specific file causing the crash.
        2. Suggest a potential git fix.
        3. Output format: JSON.
        """
        
        # Mocking the AI Response for Portfolio Demo
        print(f"--- SENDING PROMPT TO AI ---\n{user_prompt}")
        
        return {
            "root_cause": "DatabaseConnectionTimeout",
            "file": "utils/db_manager.py:45",
            "suggestion": "Increase connection_timeout in config.yaml from 5s to 30s."
        }

if __name__ == "__main__":
    # 1. Simulate a Log File
    with open("jenkins_crash.log", "w") as f:
        f.write("INFO: Build Started...\nINFO: Tests Running...\nCRITICAL FAILURE: ConnectionRefusedError\n  at utils/db_manager.py:45\n  Timeout waiting for 5432.")

    # 2. Run Analysis
    analyzer = GenAILogAnalyzer("sk-dummy-key")
    error_block = analyzer.extract_error_block("jenkins_crash.log")
    
    if error_block:
        insight = analyzer.analyze_with_llm(error_block)
        print(f"\n--- AI INSIGHT ---\n{json.dumps(insight, indent=2)}")
    else:
        print("No errors found in log.")
