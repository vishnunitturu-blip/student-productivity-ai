from database.db import add_task_db, get_tasks, delete_task_db, complete_task_db

def add_task(task, priority=0):
    add_task_db(task, priority)
    print(f"Task added: {task} (Priority: {priority})")

def show_tasks():
    tasks = get_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("Your Tasks:")
    for t in tasks:
        # t[0] = id, t[1] = task, t[2] = priority, t[3] = status
        color = "\033[92m"  # green for low
        if t[2] == 1:
            color = "\033[93m"  # orange for medium
        elif t[2] == 2:
            color = "\033[91m"  # red for high

        print(f"{color}{t[0]}. {t[1]} (Priority: {t[2]}, Status: {t[3]})\033[0m")

def delete_task(task_id):
    delete_task_db(task_id)
    print("Task deleted successfully.")

def complete_task(task_id):
    complete_task_db(task_id)
    print("Task marked as completed.")

def suggest_task():
    tasks = get_tasks(status="pending")
    if not tasks:
        return "No pending tasks."
    next_task = tasks[0]  # highest priority pending task
    return f"Next task: {next_task[1]} (Priority: {next_task[2]})"
