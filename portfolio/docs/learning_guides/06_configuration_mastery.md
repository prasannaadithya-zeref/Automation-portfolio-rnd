# ⚙️ Configuration & Inputs Guide
*How to handle Dynamic Inputs, CSVs, and Secrets like a Pro.*

## 1. The `.env` File (Secrets)
Never hardcode passwords in Python.
*   **The Problem**: `db.connect("password123")` -> You push to Git -> Hackers steal it.
*   **The Solution**:
    1.  Create a file named `.env` (See `.env.example`).
    2.  Add `DB_PASS=secret`.
    3.  Add `.env` to `.gitignore`.
    4.  **Python Code**:
        ```python
        import os
        from dotenv import load_dotenv # pip install python-dotenv
        
        load_dotenv()
        password = os.getenv("DB_PASS")
        ```

## 2. Dynamic Inputs (Command Line Args)
How to run the same script for "Dev" and "QA"?
*   **Don't change the code.** Use Arguments.
*   **Code (`portfolio/python-frameworks/main.py`)**:
    ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", help="Target Environment (DEV/QA)")
    args = parser.parse_args()
    print(f"Running in {args.env}")
    ```
*   **Run It**: `python main.py --env QA`

## 3. Handling Data Inputs (CSV/Excel)
If your test needs to run 100 times with different data:
*   **The Pattern**: Data-Driven Testing.
*   **Files**: Look at `curriculum/1_python/file_handling_mastery.py`.
    *   It detects: "Is this CSV?" -> Use Pandas.
    *   It detects: "Is this JSON?" -> Use `json.load`.

## 4. Docker Usage (The Container)
I have added a `Dockerfile` to the root.
*   **Build It**: `docker build -t my-portfolio .`
*   **Run It**: `docker run my-portfolio`
*   *Magic*: It basically creates a Linux computer inside your Windows, installs Python, and runs the `run_portfolio_demo.py`.
