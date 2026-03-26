import sqlite3

DB_NAME = "database/tasks.db"

def init_db():
    """Create tasks table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        priority INTEGER DEFAULT 0,
        status TEXT DEFAULT 'pending'
    )
    """)
    conn.commit()
    conn.close()

def add_task_db(task, priority=0):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, priority, status) VALUES (?, ?, 'pending')", (task, priority))
    conn.commit()
    conn.close()

def get_tasks(status=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if status:
        cursor.execute("SELECT id, task, priority, status FROM tasks WHERE status=? ORDER BY priority DESC, id ASC", (status,))
    else:
        cursor.execute("SELECT id, task, priority, status FROM tasks ORDER BY priority DESC, id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_task_db(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def complete_task_db(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status='completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
