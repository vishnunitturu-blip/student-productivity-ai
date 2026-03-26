import sqlite3

def add_task(task):
    conn = sqlite3.connect("database/tasks.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

    print(f"Task added: {task}")


def show_tasks():
    conn = sqlite3.connect("database/tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    if not tasks:
        print("No tasks available.")
        return

    print("Your Tasks:")
    for task in tasks:
        print(f"{task[0]}. {task[1]}")
