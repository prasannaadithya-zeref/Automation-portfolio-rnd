# 🎤 Top 30 Automation Engineer Interview Questions
*Master these, and you will sound like a Senior.*

## 🐍 Python
**Q1. What is the difference between `list` and `tuple`?**
*   **Answer**: Lists are mutable (can change), Tuples are immutable (read-only). Use Lists for data that changes, Tuples for configuration/secrets.

**Q2. What is a Decorator?**
*   **Answer**: A function that takes another function and extends its behavior without modifying it. Example: `@login_required` or `@timer`.

**Q3. How does Python manage memory?**
*   **Answer**: Private Heap space. Python uses **Reference Counting** (deletes objects when `ref_count == 0`) and a Garbage Collector for cyclic references.

## 🤖 Robot Framework
**Q4. What is the difference between Test Setup and Suite Setup?**
*   **Answer**: `Suite Setup` runs **once** per file (e.g., Open Browser). `Test Setup` runs before **every** test case (e.g., Go to Login Page).

**Q5. How do you handle dynamic elements?**
*   **Answer**: I use "Wait Until Element Is Visible" keywords or XPath contains() logic, rather than hardcoded Sleep.

## 💾 SQL
**Q6. What is the difference between `RANK` and `DENSE_RANK`?**
*   **Answer**: `RANK` skips numbers for ties (1, 1, 3). `DENSE_RANK` does not skip (1, 1, 2).

**Q7. Explain `LEFT JOIN` vs `INNER JOIN`.**
*   **Answer**: `INNER` only returns matching rows. `LEFT` returns ALL rows from the left table, even if there is no match (Result is NULL).

## 🥒 BDD (Behave)
**Q8. What is `background` in a Feature file?**
*   **Answer**: Steps that are common to all scenarios in that feature (like "Given I am logged in"). It reduces code duplication.

## ☁️ Cloud & DevOps
**Q9. What triggers your Jenkins pipeline?**
*   **Answer**: A Webhook from GitHub. Whenever code is pushed to `main`, Jenkins detects it and runs the build.

**Q10. Why use Docker?**
*   **Answer**: "It works on my machine" is not an excuse. Docker ensures the environment (OS, Python version) is exactly the same from Dev to Prod.
