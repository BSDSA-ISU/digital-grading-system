import sqlite3

def ShowAll():
    con = sqlite3.connect("students.db")
    cursor = con.cursor()

    cursor.execute("select * from students;")
    x= cursor.fetchall()

    for i in x:
        print(i[0])

def Insert(program, age, study_hours, attenndance_rate, quiz_score, midterm_score, final_score, status, gpa, grade : int):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Commands execute
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE,
            program TEXT,
            grade INTEGER,
            status TEXT,

            age INTEGER,
            study_hours INTEGER,
            attendance_rate REAL,
            quiz_score INTEGER,
            midterm_score INTEGER,
            final_score INTEGER,
            gpa REAL
        );
    """)
    cursor.execute("INSERT INTO Data (program, status, age, study_hours, attendance_rate, quiz_score, midterm_score, final_score, gpa, grade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (program, status, age, study_hours, attenndance_rate, quiz_score, midterm_score, final_score, gpa, grade))
    conn.commit()
    conn.close()

def delete():
    pass


ShowAll()