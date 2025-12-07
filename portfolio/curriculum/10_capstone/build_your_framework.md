# 🏗️ CAPSTONE: Build Your Own Hybrid Framework
*The Final Exam. Do not copy code. Write this from scratch.*

## The Goal
Build a framework that tests a dummy login page, validates the database, and reports to Slack.

## Step 1: Structure
Create this folder structure:
```
my_framework/
  ├── drivers/ (chromedriver)
  ├── pages/ (Page Object Models)
  ├── tests/ (Robot/Pytest files)
  ├── utils/ (DB/API helpers)
  └── config.yaml
```

## Step 2: The Core (Python)
Write a class `DatabaseWrapper` in `utils/db.py`.
*   It must follow the **Singleton Pattern** (One connection per app).
*   It must read credentials from `config.yaml`.

## Step 3: The Logic (Robot)
Write `tests/login_test.robot`.
*   Use `SeleniumLibrary`.
*   Import your `DatabaseWrapper` as a Library.
*   **Scenario**:
    1.  Login to Website.
    2.  Query DB: `SELECT status FROM users WHERE name='myuser'`.
    3.  Assert that Web Status == DB Status.

## Step 4: The CI/CD
Write a `Jenkinsfile`.
*   Stage 1: `pip install -r requirements.txt`
*   Stage 2: `robot tests/`
*   Stage 3: Archive Reports.

## Checklist for Senior Quality
1.  [ ] Did you hardcode passwords? (Fail if yes).
2.  [ ] Is there a `README.md`?
3.  [ ] Do you catch exceptions in your Python code?

*If you can build this without looking at the reference code, you are hired.*
