# 🥒 Behave (BDD) Masterclass

**Behavior Driven Development (BDD)** is about collaboration. We write tests in "Plain English" so Product Managers can read them.

## 1. The Gherkin Syntax (`.feature`)
Gherkin uses 3 main keywords:
*   **GIVEN**: The initial state (Preconditions).
    *   `Given I am on the login page`
*   **WHEN**: The action.
    *   `When I enter valid credentials`
*   **THEN**: The expected result.
    *   `Then I should be redirected to the dashboard`

## 2. The Glue Code (`steps.py`)
This is the Python code that executes when Behave reads a line.

```python
# steps/login_steps.py
from behave import given, when, then

@given('I am on the login page')
def step_open_login(context):
    context.driver.get("https://site.com/login")
```

## 3. Hooks (`environment.py`)
Think of these as "Setup" and "Teardown".
*   `before_all(context)`: Runs once before everything.
*   `before_scenario(context)`: Runs before every test.
*   `after_scenario(context)`: Runs after every test (Good for screenshots!).

## [HANDS ON TASK]
1.  Go to `portfolio/behave-bdd/features/ui_login.feature`.
2.  Add a generic scenario: "Login with BLANK password".
3.  Run `behave` in the terminal and see it fail (Red).
