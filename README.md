Of course. Here is a complete README file for your project, documenting the entire process from installation to final usage with an AI. You can copy and paste this directly into a `README.md` file in your GitHub repository.

-----

# HR Leave Manager MCP Server

This project is a simple, tool-based server built with the `fastmcp` library to manage employee leave requests. It exposes several tools that can be used by an AI model, such as Anthropic's Claude, to interact with a mock employee database.

## Features

  * ✅ **Check Leave Balance:** Instantly see the remaining leave days for any employee.
  * ✅ **Apply for Leave:** Submit leave requests for employees, which automatically updates their balance.
  * ✅ **View Leave History:** Retrieve a complete history of an employee's past leave dates.
  * ✅ **Get All Employee Details:** Fetch a complete record for an employee, including balance and history.

-----

## ⚙️ Setup and Installation

Follow these steps to set up the project on a new machine.

**1. Prerequisites**
* You must have **Python 3.8+** installed.
* You must have **Claude Desktop** installed.
* You need **uv**, an extremely fast Python package installer. If you don't have it, run this command:
  ```bash
  curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

-----

## ⚙️ Setup and Installation

Follow these steps to set up the project on your local machine.

### 1\. Install `uv`

If you don't have `uv` installed, run the following command in your terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*(For other installation methods, see the [official `uv` documentation](https://www.google.com/search?q=%5Bhttps://github.com/astral-sh/uv%23installation%5D\(https://github.com/astral-sh/uv%23installation\)).)*

### 2\. Clone the Repository

Clone your repository to your local machine:

```bash
git clone <your-github-repo-url>
cd <your-repo-name>
```

### 3\. Install Dependencies

Use `uv` to create a virtual environment and install the required `fastmcp` package:

```bash
uv pip install fastmcp
```

-----

## 🚀 Usage

There are two primary ways to use this project: for local testing via the command line and as a tool server for an AI like Claude.

### 1\. Local Testing (Interactive CLI)

This method is for quickly testing the logic of your functions without needing an AI.

**A. Start the Interactive Session:**
Run the following command to start a Python interactive session (REPL) inside the project's virtual environment:

```bash
uv run python
```

Your prompt will change to `>>>`.

**B. Import and Call Your Tools:**
Now you can import your functions from `main.py` and call them directly.

```python
# First, import the functions
>>> from main import get_leave_balance, apply_leave, get_employee_details

# Now, call them as needed
>>> get_leave_balance("E001")
'Employee E001 has 18 leave days remaining.'

>>> apply_leave("E002", ["2025-10-01"])
'✅ Leave approved for 1 day(s). New balance: 19.'

>>> get_employee_details("E002")
{'balance': 19, 'history': ['2025-10-01']}
```

To exit the session, type `exit()`.

### 2\. Running with an AI Client (Claude Desktop App)

This is the intended use case, where the AI acts as the client.

**A. Provide the Code:**
Copy the entire contents of your `main.py` file.

**B. Add to Claude:**
In the Claude desktop app, paste your code into the section for providing tools or files. The platform will run the script in the background, making the tools available to the AI.

**C. Prompt the AI in Natural Language:**
You can now ask Claude to perform actions using your tools. For example:

  * "How many vacation days does employee E001 have left?"
  * "File a leave request for E003 for July 20th, 2025."
  * "Show me the complete leave history for employee E003."

-----

## 🛠️ Tools Overview

| Tool Name            | Description                                                       | Example Parameters                                   |
| -------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| `apply_leave`        | Applies for leave for one or more dates for a specific employee.  | `employee_id="E003"`, `leave_dates=["2025-07-21"]`    |
| `get_leave_balance`  | Checks the remaining leave day balance for an employee.           | `employee_id="E001"`                                 |
| `get_leave_history`  | Gets the leave history for a specific employee.                   | `employee_id="E002"`                                 |
| `get_employee_details` | Gets all leave data for an employee, including balance and history. | `employee_id="E003"`                                 |