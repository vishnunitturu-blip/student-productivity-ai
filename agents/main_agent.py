from agents.task_agent import add_task, show_tasks

def run_agent():
    print("Student Productivity AI Started")

    while True:
        command = input("\nEnter command (add/show/exit): ").strip().lower()

        if command == "add":
            task = input("Enter task: ")
            add_task(task)

        elif command == "show":
            show_tasks()

        elif command == "exit":
            print("Exiting Productivity AI")
            break

        else:
            print("Invalid command")
