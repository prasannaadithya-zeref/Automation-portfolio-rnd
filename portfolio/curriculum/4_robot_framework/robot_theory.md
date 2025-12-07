# 🤖 Robot Framework Theory

## 1. Architecture
*   **Layer 1 (Tests)**: `.robot` files. High-level English.
*   **Layer 2 (Keywords)**: Reusable steps like `Login App`.
*   **Layer 3 (Libraries)**: Python code (`SeleniumLibrary`) that does the heavy lifting.

## 2. Variable Scopes
*   **Global Variables**: Available everywhere (usually defined in Command Line).
*   **Suite Variables**: Available in all tests in one file.
*   **Test Variables**: Available only in current test case.

## 3. Tags
*   `@smoke`: Critical path tests. Run with `robot -i smoke tests/`.
*   `@regression`: Full suite.

## 4. Setup & Teardown
*   `Suite Setup`: Runs ONCE before all tests (e.g., Open Browser).
*   `Test Setup`: Runs before EACH test (e.g., Go to Home Page).
*   `Test Teardown`: Runs after EACH test (e.g., Screenshot on Failure).
