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


def update_student(db_name="student_grade.db", student_id=None, **updates):
    """
    Update a student record based on student_id.
    Pass the columns to update as keyword arguments.
    Example:
        update_student(student_id="S123", grade=95, gpa=3.7)
    """
    if not student_id:
        print("You must provide a student_id to update.")
        return

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Prepare the SET clause dynamically
    set_clause = ", ".join([f"{col} = ?" for col in updates.keys()])
    values = list(updates.values())
    values.append(student_id)  # For the WHERE clause

    cur.execute(f"""
        UPDATE students
        SET {set_clause}
        WHERE student_id = ?;
    """, values)

    conn.commit()

    # Show the updated row (id and student_id included)
    cur.execute("SELECT id, student_id, * FROM students WHERE student_id = ?;", (student_id,))
    row = cur.fetchone()
    headers = [desc[0] for desc in cur.description]
    print(tabulate([row], headers=headers, tablefmt="grid"))

    conn.close()

def find_students(db_name="student_grade.db", student_id_partial=""):
    """
    Search students by partial student_id and display their id and student_id.
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Use LIKE for partial matching
    cur.execute("""
        SELECT id, student_id, program
        FROM students
        WHERE student_id LIKE ?;
    """, (f"%{student_id_partial}%",))

    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]

    if rows:
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No matching students found.")

    conn.close()

def show_specific_student(db_name="student_grade.db", student_id_partial=""):
    """
    Search students by partial student_id and display their id and student_id.
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Use LIKE for partial matching
    cur.execute("""
        SELECT * FROM students
        WHERE student_id LIKE ?;
    """, (f"%{student_id_partial}%",))

    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]

    if rows:
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No matching students found.")

    conn.close()

def delete_student(db_name="student_grade.db", student_id_partial=""):
    """
    Search students by partial student_id and delete a selected record.
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Search for students
    cur.execute("""
        SELECT id, student_id, program
        FROM students
        WHERE student_id LIKE ?;
    """, (f"%{student_id_partial}%",))

    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]

    if not rows:
        print("No matching students found.")
        conn.close()
        return

    print(tabulate(rows, headers=headers, tablefmt="grid"))

    # Ask user which student to delete
    try:
        student_id_to_delete = input("Enter the student_id to delete (exact match): ").strip()
        cur.execute("SELECT * FROM students WHERE student_id = ?;", (student_id_to_delete,))
        row = cur.fetchone()
        if not row:
            print("Invalid student_id. No record deleted.")
        else:
            cur.execute("DELETE FROM students WHERE student_id = ?;", (student_id_to_delete,))
            conn.commit()
            print(f"Student with student_id {student_id_to_delete} has been deleted.")
    except Exception as e:
        print("Error:", e)

    conn.close()

