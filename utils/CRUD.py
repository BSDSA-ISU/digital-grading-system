import sqlite3
from tabulate import tabulate

def setup_database(db_name="student_grade.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            student_id TEXT UNIQUE,
            program TEXT,
            grade REAL,
            status INTEGER,
            age INTEGER,
            attendance_rate REAL,
            quiz_score REAL,
            exams_score REAL,
            performance_task REAL,
            activities REAL,
            final_grade REAL,
            gpa REAL
        );
    """)
    conn.commit()
    return conn

def insert_student(db_name="student_grade.db", **student_info):
    """
    Insert a student record into the database.

    Expected keys in student_info:
    student_id, program, grade, status, age, attendance_rate,
    quiz_score, exams_score, performance_task, activities,
    final_grade, gpa
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    fields = (
        "student_id", "program", "grade", "status", "age",
        "attendance_rate", "quiz_score", "exams_score",
        "performance_task", "activities", "final_grade", "gpa"
    )

    values = [student_info.get(f) for f in fields]

    cur.execute(f"""
        INSERT INTO students ({", ".join(fields)})
        VALUES ({", ".join(["?"] * len(fields))});
    """, values)

    conn.commit()
    conn.close()

def ShowCol(filename="students.db"):

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()

    headers = [desc[0] for desc in cursor.description]

    print(tabulate(rows, headers=headers, tablefmt="grid"))


