tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
