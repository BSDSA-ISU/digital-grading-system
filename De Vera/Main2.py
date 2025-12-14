import sqlite3
import random
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Connect to SQLite
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    subject TEXT NOT NULL,
    deadline TEXT,
    status TEXT
)
""")
conn.commit()

# SUBJECTS (UPDATED ✅)
SUBJECTS = [
    "Programming for Data Science",
    "Computer-Aided Statistical Inference",
    "Linear Algebra for Data Science",
    "Data Structures and Algorithms",
    "Technology and Society"
]

# RANDOM TASK TITLES
TASK_TITLES = [
    "Finish Assignment",
    "Study for Quiz",
    "Project Research",
    "Prepare Presentation",
    "Write Case Study",
    "Review Notes",
    "Compile Codes",
    "Analyze Dataset",
    "Submit Report"
]

# RANDOM STATUSES
STATUSES = ["Pending", "Done"]

# ✅ AUTO-INSERT RANDOM DATA FUNCTION
def insert_random_data():
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        for _ in range(10):
            title = random.choice(TASK_TITLES)
            subject = random.choice(SUBJECTS)
            deadline = f"2025-12-{random.randint(1, 28)}"
            status = random.choice(STATUSES)

            cursor.execute(
                "INSERT INTO tasks (title, subject, deadline, status) VALUES (?, ?, ?, ?)",
                (title, subject, deadline, status)
            )
        conn.commit()
        print("✅ Random sample database created!\n")

insert_random_data()

# Visualization
def Visual():
    conn = sqlite3.connect("todo.db")
    df = pd.read_sql_query("SELECT status FROM tasks", conn)
    sns.countplot(x='status', data=df, palette='magma')
    plt.title("Pending tasks and done tasks")
    plt.ylabel("count")
    plt.show()

# Add Task
def add_task():
    title = input("Enter task title: ")

    print("\nSubjects:")
    for i, sub in enumerate(SUBJECTS, 1):
        print(f"{i}. {sub}")

    choice = int(input("Choose subject number: "))
    subject = SUBJECTS[choice - 1]

    deadline = input("Enter deadline (YYYY-MM-DD): ")
    if not "-" in deadline or len(deadline) <= 10:
        print("Invalid date")
        sys.exit(1)

    cursor.execute(
        "INSERT INTO tasks (title, subject, deadline, status) VALUES (?, ?, ?, ?)",
        (title, subject, deadline, "Pending")
    )
    conn.commit()
    print("✅ Task added successfully!\n")

# View Tasks
def view_tasks():
    print("\nChoose subject:")
    for i, sub in enumerate(SUBJECTS, 1):
        print(f"{i}. {sub}")

    choice = int(input("Enter number: "))
    subject = SUBJECTS[choice - 1]

    cursor.execute("SELECT * FROM tasks WHERE subject = ?", (subject,))
    rows = cursor.fetchall()

    if not rows:
        print("\nNo tasks found.\n")
    else:
        print("\nID | Title | Deadline | Status")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[3]} | {row[4]}")
        print()

# Update Task
def update_task():
    task_id = int(input("Enter task ID to update: "))
    new_title = input("New title: ")
    new_deadline = input("New deadline (YYYY-MM-DD): ")

    cursor.execute(
        "UPDATE tasks SET title=?, deadline=? WHERE id=?",
        (new_title, new_deadline, task_id)
    )
    conn.commit()
    print("✅ Task Updated!\n")

# Update Status
def update_status():
    task_id = int(input("Enter task ID: "))
    status = input("Enter new status (Done / Pending): ")

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        (status, task_id)
    )
    conn.commit()
    print("✅ Status Updated!\n")

# Delete Task
def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("✅ Task Deleted!\n")

# Main Menu
def menu():
    while True:
        print("""
====== TASK MANAGEMENT SYSTEM ======
1. Add Task
2. View Tasks by Subject
3. Update Task
4. Update Status
5. Delete Task
6. Visualization
7. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            update_status()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            Visual()
        elif choice == "7":
            print("bye")
            sys.exit(0)
        else:
            print("❌ Invalid choice.\n")

menu()
conn.close()

