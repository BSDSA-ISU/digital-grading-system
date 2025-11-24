import random
import sqlite3

def setup_database(db_name="students.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
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

    conn.commit()
    return conn


def generate_student_record():
    programs = ["BSCS", "BSDSA", "BSIT", "BLIS"]
    weights = [0.4, 0.1, 0.4, 0.1]

    student_id = f"2025-{random.randint(100000, 999999)}"

    # base pass/fail grade
    roll = random.random()
    if roll < 0.10:
        grade = random.randint(95, 100)
    elif roll < 0.80:
        grade = random.randint(75, 94)
    else:
        grade = random.randint(50, 74)

    status = "Passed" if grade >= 75 else "Failed"
    program = random.choices(programs, weights=weights, k=1)[0]

    age = random.randint(18, 25)
    study_hours = random.randint(0, 40)
    attendance_rate = round(random.uniform(40, 100), 2)

    # quiz, midterm, final depend on study_hours & attendance a bit
    base = (study_hours * 1.2) + (attendance_rate * 0.5)

    quiz_score = max(0, min(100, int(base + random.gauss(0, 10))))
    midterm_score = max(0, min(100, int(base + random.gauss(0, 12))))
    final_score = max(0, min(100, int(base + random.gauss(0, 15))))

    # GPA depends on exams + study + attendance
    # it's not perfect, but at least it won't look like confetti
    gpa_raw = (
        quiz_score * 0.2 +
        midterm_score * 0.3 +
        final_score * 0.4 +
        study_hours * 0.3 +
        attendance_rate * 0.1
    ) / 25

    gpa = round(max(1.0, min(4.0, gpa_raw)), 2)

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
    print("Dataset ready. Go impress someone who doesn’t know better.")
