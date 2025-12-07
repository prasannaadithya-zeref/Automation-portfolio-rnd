import subprocess
import time
import os
import sys

def start_mock_api():
    """Starts Flask app in a separate process."""
    print("[RUNNER] Starting Mock API on port 5000...")
    return subprocess.Popen([sys.executable, "python-frameworks/api_mock/app.py"], 
                            cwd="portfolio", 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)

def run_python_frameworks():
    print("\n" + "="*50)
    print(" STEP 1: Running Python Framework Demos")
    print("="*50)
    # Ensure reports go to root/reports. Since we CWD into python-frameworks, output must be ../reports
    output_path = os.path.abspath("reports")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    subprocess.run([sys.executable, "main.py", "--env", "QA", "--run_api_tests", "--report_dir", output_path], 
                   cwd="python-frameworks")

def run_robot_tests():
    print("\n" + "="*50)
    print(" STEP 2: Running Robot Framework Tests")
    print("="*50)
    try:
        output_path = os.path.abspath("reports/robot")
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.abspath("python-frameworks")
        subprocess.run(["robot", "--outputdir", output_path, "robot-framework/tests/integration_suite.robot"], shell=True, env=env)
        print(f"[RUNNER] Robot reports saved to: {output_path}")
    except Exception as e:
        print(f"[RUNNER] Failed to run robot: {e}")

def run_behave_tests():
    print("\n" + "="*50)
    print(" STEP 3: Running Behave BDD Tests")
    print("="*50)
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.abspath("python-frameworks")
        # Ensure result file location
        # Behave uses -o for output file, or --junit --junit-directory
        subprocess.run(["behave", "behave-bdd/features/aws_etl.feature", "--junit", "--junit-directory", "reports/behave"], shell=True, env=env)
        print("[RUNNER] Behave JUnit reports saved to: reports/behave")
    except Exception as e:
        print(f"[RUNNER] Failed to run behave: {e}")

if __name__ == "__main__":
    print(">>> PORTFOLIO 'CLICK RUN' DEMO <<<")
    
    # Create central reports dir
    if not os.path.exists("reports"):
        os.makedirs("reports")

    api_process = None
    try:
        api_process = subprocess.Popen([sys.executable, "python-frameworks/api_mock/app.py"])
        time.sleep(3)
        
        run_python_frameworks()
        run_robot_tests()
        run_behave_tests()
        
    finally:
        print("\n" + "="*50)
        print(" DEMO COMPLETE ")
        print("="*50)
        print(f"CHECK RESULTS HERE: {os.path.abspath('reports')}")
        print("1. execution_summary.html (Python Frameworks)")
        print("2. robot/report.html (Robot Framework)")
        print("3. behave/ (BDD Results)")
        
        if api_process:
            api_process.terminate()
        sys.exit(0)
