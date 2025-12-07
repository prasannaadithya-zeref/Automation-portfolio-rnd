# 🤖 Prompt Engineering for SDETs
*How to use GenAI to write tests 10x faster (Vibe Coding).*

## 1. The "Auto-Generation" Workflow
Don't write boilerplates. Generate them.

**Bad Prompt**:
> "Write a test for login."

**Professional SDET Prompt**:
> "Act as a Senior QA Automation Engineer using Robot Framework.
> Write a test suite for the 'Login Page' based on the following requirements:
> 1. Use Page Object Model keywords (e.g., `LoginPage.Input Password`).
> 2. Handle 3 scenarios: Valid Login, Invalid Password, SQL Injection Attempt.
> 3. Use Data-Driven testing style.
> Output code only."

## 2. Chain of Thought (CoT) Debugging
When you paste an error to ChatGPT, guide it.

**Prompt Strategy**:
> "I am facing a `StaleElementReferenceException` in Selenium.
> 1. Explain WHY this happens architecturally (DOM updates).
> 2. Analyze my code snippet below.
> 3. Provide 3 solutions (Retry logic, Refresh, Explicit Wait).
> [Insert Code]"

## 3. "Vibe Coding" in CI/CD
We can inject AI into our Jenkins Pipeline.
*   **Step 1**: Test Fails.
*   **Step 2**: Jenkins grabs the `log.html`.
*   **Step 3**: Python script sends log to OpenAI API.
*   **Step 4**: AI posts a comment on the Pull Request: *"Tests failed because you renamed the ID 'submit-btn' to 'login-btn'. Please revert."*

## 4. RAG for Documentation
*Retreival Augmented Generation.*
Imagine chatting with this Repo.
*   "Hey Bot, where is the function that handles Oracle connections?"
*   Bot searches `db_manager.py` embedding and answers: "It's in `DatabaseManager.get_engine` using SQLAlchemy."
