import random
import sqlite3
import numpy as np

def setup_database(db_name="students.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

def generate_student_raw():
    programs = ["BSCS", "BSDSA", "BSIT", "BLIS"]
    weights = [0.4, 0.1, 0.4, 0.1]

    student = {}
    student['student_id'] = f"2025-{random.randint(100000, 999999)}"
    student['program'] = random.choices(programs, weights=weights, k=1)[0]
    student['age'] = random.randint(18, 25)
    student['attendance_rate'] = round(random.uniform(40, 100), 2)

    # Base score for randomness
    base = student['attendance_rate'] * 0.5

    # Individual scores with Gaussian noise
    student['quiz_score'] = np.round(np.clip(base + np.random.normal(50, 10), 0, 100), 5)
    student['exams_score'] = np.round(np.clip(base + np.random.normal(50, 10), 0, 100), 5)
    student['performance_task'] = np.round(np.clip(base + np.random.normal(50, 25), 0, 100), 5)
    student['activities'] = np.round(np.clip(base/2 + np.random.normal(25, 5), 0, 50), 5)

    # Raw weighted score for rank-based final grade assignment
    student['raw_score'] = (student['quiz_score']*0.15 +
                            student['exams_score']*0.25 +
                            student['performance_task']*0.5 +
                            student['activities']*0.1)
    return student

def assign_final_grades(students):
    """Assign smooth final grades while keeping realistic bottom spread and ~85% pass."""
    students_sorted = sorted(students, key=lambda x: x['raw_score'])
    n = len(students_sorted)

    for i, s in enumerate(students_sorted):
        rank_frac = i / n

        # Realistic failers spread (55-75)
        if rank_frac < 0.15:
            s['final_grade'] = np.round(
                np.clip(55 + 20 * (rank_frac/0.15) + np.random.normal(0,2), 0, 75), 5
            )
        # Mid students (80-89)
        elif rank_frac < 0.85:
            mid_frac = (rank_frac - 0.15)/0.7
            s['final_grade'] = np.round(
                80 + 9 * mid_frac + np.random.normal(0,0.5), 5
            )
        # Top students (90-100)
        else:
            top_frac = (rank_frac - 0.85)/0.15
            s['final_grade'] = np.round(
                90 + 10 * top_frac + np.random.normal(0,0.5), 5
            )

        # Weighted final grade with proper percentages
        # Weighted final grade with proper percentages
# Weighted final grade
        weighted_grade = (
            s['quiz_score']*0.15 +
            s['exams_score']*0.25 +
            s['performance_task']*0.5 +
            s['activities']*0.2
        )

# --- Adaptive noise with ceiling compression ---
        if weighted_grade >= 95:
            # scale top grades: 95→100 range is compressed to 95→99
            weighted_grade = 95 + (weighted_grade - 95) * 0.8
            noise = np.random.normal(0, 0.3)  # very light noise
        elif weighted_grade >= 90:
            noise = np.random.normal(0, 1.0)
        else:
            noise = np.random.normal(0, 1.5)

        # Apply noise
        s['final_grade'] = np.round(np.clip(weighted_grade + noise, 0, 100), 5)

        # Performance task make-or-break
        if s['performance_task'] < 10:
            s['final_grade'] = min(s['final_grade'], 75)

# Status & grade
        s['status'] = 1 if s['final_grade'] >= 76 else 0
        s['grade'] = s['final_grade']



        # GPA (reverse scale)
        perf = (s['quiz_score']*0.2 + s['exams_score']*0.3 +
                s['final_grade']*0.4 + s['attendance_rate']*0.1)
        s['gpa'] = np.round(np.clip(5 - perf/25, 1, 5), 5)

    return students_sorted

def insert_random_students(conn, count=300):
    cur = conn.cursor()
    
    students = [generate_student_raw() for _ in range(count)]
    students = assign_final_grades(students)

    for s in students:
        try:
            cur.execute("""
                INSERT INTO students (
                    student_id, program, grade, status,
                    age, attendance_rate,
                    quiz_score, exams_score, performance_task, activities,
                    final_grade, gpa
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                s['student_id'], s['program'], s['grade'], s['status'],
                s['age'], s['attendance_rate'],
                s['quiz_score'], s['exams_score'], s['performance_task'], s['activities'],
                s['final_grade'], s['gpa']
            ))
        except sqlite3.IntegrityError:
            continue

    conn.commit()

if __name__ == "__main__":
    conn = setup_database()
    insert_random_students(conn, 2001)
    print("Dataset ready: realistic bottom spread, top 90–100, ~85% pass, smooth decimals.")
