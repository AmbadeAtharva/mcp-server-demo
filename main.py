# To run this code, first install FastMCP: uv pip install fastmcp
from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any

# In-memory mock database with 20 leave days to start
employee_leaves: Dict[str, Dict[str, Any]] = {
    "E001": {"balance": 18, "history": ["2024-12-25", "2025-01-01"]},
    "E002": {"balance": 20, "history": []},
    "E003": {"balance": 5, "history": ["2025-03-10", "2025-03-11", "2025-03-12"]}
}

# Create an MCP server instance
mcp = FastMCP("LeaveManager")

# --- All functions are now defined as Tools for maximum compatibility ---

@mcp.tool()
def apply_leave(employee_id: str, leave_dates: List[str]) -> str:
    """
    Apply for leave for one or more dates for a specific employee.
    Example: apply_leave(employee_id="E003", leave_dates=["2025-07-21"])
    """
    if employee_id not in employee_leaves:
        return f"Error: Employee ID '{employee_id}' not found."

    requested_days = len(leave_dates)
    if requested_days == 0:
        return "Error: No leave dates were provided."
        
    available_balance = employee_leaves[employee_id]["balance"]

    if available_balance < requested_days:
        return (f"Insufficient leave balance. You requested {requested_days} day(s) "
                f"but have only {available_balance} left.")

    # Update balance and add dates to history
    employee_leaves[employee_id]["balance"] -= requested_days
    employee_leaves[employee_id]["history"].extend(leave_dates)

    new_balance = employee_leaves[employee_id]['balance']
    return f"✅ Leave approved for {requested_days} day(s). New balance: {new_balance}."

@mcp.tool()
def get_leave_balance(employee_id: str) -> str:
    """Check the remaining leave day balance for an employee."""
    if employee_id in employee_leaves:
        balance = employee_leaves[employee_id]['balance']
        return f"Employee {employee_id} has {balance} leave days remaining."
    return f"Error: Employee ID '{employee_id}' not found."

@mcp.tool()
def get_leave_history(employee_id: str) -> str:
    """Get the leave history for a specific employee."""
    if employee_id in employee_leaves:
        history = employee_leaves[employee_id]['history']
        if not history:
            return f"Employee {employee_id} has no leave history."
        # Format the list of dates into a readable string
        return f"Leave history for {employee_id}: {', '.join(history)}"
    return f"Error: Employee ID '{employee_id}' not found."
    
@mcp.tool()
def get_employee_details(employee_id: str) -> Dict[str, Any]:
    """Get all leave data for an employee, including balance and history."""
    if employee_id in employee_leaves:
        return employee_leaves[employee_id]
    return {"error": f"Employee ID '{employee_id}' not found."}

@mcp.tool()
def get_greeting(name: str) -> str:
    """Get a personalized greeting."""
    return f"Hello, {name}! Welcome to the Leave Management system. 🌴"


if __name__ == "__main__":
    print("🌴 HR Leave Manager MCP Server is running...")
    print("Available tools:")
    # Now all functions will be listed as tools
    for tool_name, tool in mcp.tools.items():
        # Get the docstring to show what the tool does
        docstring = tool.fn.__doc__.strip().split('\n')[0] if tool.fn.__doc__ else "No description."
        print(f"  - {tool_name}: {docstring}")
    
    mcp.run()