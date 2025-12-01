import sqlite3
import random

def setup_database():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            program TEXT,
            grade TEXT,
            status INTEGER,
            age INTEGER,
            study_hours REAL,
            attendance_rate REAL,
            quiz_score REAL,
            midterm_score REAL,
            final_score REAL,
            gpa REAL
        )
    """)

    conn.commit()
    return conn


def generate_student_record():
    student_id = f"STU{random.randint(1000, 9999)}"
    program = random.choice(["BSIT", "BSBA", "BSA", "BSED", "BSHM", "BSN"])
    grade = random.choice(["1st Year", "2nd Year", "3rd Year", "4th Year"])

    age = random.randint(17, 25)
    study_hours = round(random.uniform(0, 5), 2)
    attendance_rate = round(random.uniform(60, 100), 2)

    quiz_score = random.randint(40, 100)
    midterm_score = random.randint(40, 100)

    # Gaussian noise final score (from your original code)
    base = (quiz_score + midterm_score) / 2
    final_score = max(0, min(100, int(base + random.gauss(0, 15))))

    # --- REVERSED GPA SYSTEM ---
    # 1.0 = highest
    # >3.0 = failing

    # Same performance formula you used (bigger = better)
    performance = (
        quiz_score * 0.2 +
        midterm_score * 0.3 +
        final_score * 0.4 +
        attendance_rate * 0.1
    )

    # Convert performance → GPA (smaller = better)
    gpa_raw = 5 - (performance / 25)

    # Clamp to PH GPA scale
    gpa = round(max(1.0, min(5.0, gpa_raw)), 2)

    # GPA-based passing
    status = 1 if gpa <= 3.0 else 0

    return (
        student_id, program, grade, status,
        age, study_hours, attendance_rate,
        quiz_score, midterm_score, final_score, gpa
    )


def insert_random_students(conn, count=300):
    cur = conn.cursor()

    for _ in range(count):
        record = generate_student_record()

        try:
            cur.execute("""
                INSERT INTO students (
                    student_id, program, grade, status,
                    age, study_hours, attendance_rate,
                    quiz_score, midterm_score, final_score, gpa
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, record)
        except sqlite3.IntegrityError:
            continue

    conn.commit()


# Example run
if __name__ == "__main__":
    conn = setup_database()
    insert_random_students(conn, 50)
    print("Dataset ready. GPA scale fixed. Go impress someone who knows GPA now.")
