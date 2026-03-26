from agents.task_agent import add_task, show_tasks, delete_task, complete_task, suggest_task
from database.db import init_db

def run_agent():
    # Initialize DB
    init_db()

    # Show suggestion if any
    print(suggest_task())  # Optional: Make sure DB exists

    while True:
        cmd = input("Enter command (add/show/delete/complete/priority/exit): ").strip().lower()

        if cmd == "add":
            task = input("Enter task: ")
            priority = input("Enter priority (0=low,1=medium,2=high): ")
            try:
                priority = int(priority)
            except:
                priority = 0
            add_task(task, priority)

        elif cmd == "show":
            show_tasks()

        elif cmd == "delete":
            try:
                task_id = int(input("Enter task number: "))
                delete_task(task_id)
            except:
                print("Invalid task number!")

        elif cmd == "complete":
            try:
                task_id = int(input("Enter task number: "))
                complete_task(task_id)
            except:
                print("Invalid task number!")

        elif cmd == "priority":
            print("Feature coming soon")

        elif cmd == "exit":
            print("Exiting Productivity AI")
            break

        else:
            print("Invalid command!")
