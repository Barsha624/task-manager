import sqlite3
import os


def get_connection():
    os.makedirs("data", exist_ok=True)
    connection = sqlite3.connect("data/tasks.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


create_table()

def add_task(title):
    connection = get_connection()

    connection.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    connection.commit()
    connection.close()

def get_all_tasks():
    connection = get_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks"
    ).fetchall()

    connection.close()

    return tasks

def delete_task(task_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

def update_task(task_id, title, completed):
    connection = get_connection()

    connection.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (title, completed, task_id)
    )

    connection.commit()
    connection.close()    
    
create_table()