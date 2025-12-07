# 🤖 Robot Framework Keyword Reference & Links

This is your cheat sheet. Do not memorize these. Just know where to find them.

## 1. Standard Libraries (Built-in)
*Included with Robot Framework. No installation needed.*

| Library | Purpose | Documentation Link |
| :--- | :--- | :--- |
| **BuiltIn** | `Log`, `Should Be Equal`, `Sleep`, `Set Variable` | [Link](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) |
| **Collections** | List/Dict operations: `Append To List`, `Dictionary Should Contain Key` | [Link](https://robotframework.org/robotframework/latest/libraries/Collections.html) |
| **String** | Text manipulation: `Split String`, `Replace String`, `Get Substring` | [Link](https://robotframework.org/robotframework/latest/libraries/String.html) |
| **OperatingSystem** | File operations: `Create File`, `Get File`, `Run`, `Directory Should Exist` | [Link](https://robotframework.org/robotframework/latest/libraries/OperatingSystem.html) |
| **DateTime** | Date math: `Get Current Date`, `Add Time To Date` | [Link](https://robotframework.org/robotframework/latest/libraries/DateTime.html) |

## 2. External Libraries (must `pip install`)
*Industry Standard libraries you will use daily.*

### 🕷️ SeleniumLibrary (Web UI)
*   **Install**: `pip install robotframework-seleniumlibrary`
*   **Docs**: [SeleniumLibrary Docs](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
*   **Top Keywords**:
    *   `Open Browser  url  chrome`
    *   `Input Text  locator  text`
    *   `Click Element  locator`
    *   `Wait Until Element Is Visible  locator`

### 🔌 RequestsLibrary (API)
*   **Install**: `pip install robotframework-requests`
*   **Docs**: [RequestsLibrary Docs](https://marketsquare.github.io/robotframework-requests/doc/RequestsLibrary.html)
*   **Top Keywords**:
    *   `Create Session  alias  url`
    *   `GET On Session  alias  /endpoint`
    *   `POST On Session  alias  /endpoint  json=${data}`

### 📂 DatabaseLibrary (SQL)
*   **Install**: `pip install robotframework-databaselibrary`
*   **Docs**: [DatabaseLibrary Docs](https://marketsquare.github.io/robotframework-databaselibrary/doc/DatabaseLibrary.html)
*   **Top Keywords**:
    *   `Connect To Database`
    *   `Execute SQL String`
    *   `Check If Exists In Database`

## 3. How to create your OWN Keywords?
Refer to `curriculum/4_robot_framework/level_3_advanced.robot`.
Basically, any Python function `def my_cool_keyword(arg):` automatically becomes `My Cool Keyword` in Robot!
