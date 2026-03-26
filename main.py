from agents.main_agent import run_agent

if __name__ == "__main__":
    print("Starting Student Productivity AI")
    run_agent()
from agents.task_agent import add_task, show_tasks

add_task("Study Java")
add_task("Finish DBMS assignment")

show_tasks()
