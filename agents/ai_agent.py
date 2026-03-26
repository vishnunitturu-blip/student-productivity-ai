from database.db import get_tasks

def suggest_task():
    tasks = get_tasks(status="pending")
    if not tasks:
        return "No pending tasks. Take a break!"
    high_priority = [t for t in tasks if t[3] == 2]
    if high_priority:
        return f"AI Suggestion: Focus on: {high_priority[0][1]}"
    return f"AI Suggestion: Next task: {tasks[0][1]}"
