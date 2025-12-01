import sqlite3
import numpy as np
from sklearn.linear_model import LinearRegression

# --- Load data from the database ---
def load_student_data(db_name="students.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
        SELECT attendance_rate, quiz_score,
         exams_score, performance_task, activities, final_grade FROM students
    """)
    data = cur.fetchall()
    conn.close()
    X = np.array([row[:-1] for row in data])  # features
    y = np.array([row[-1] for row in data])   # final_grade
    return X, y

# --- Train linear regression model ---
def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

# --- Interactive grade predictor ---
def predict_grade(model):
    print("Enter student info to predict final grade:")
    #study_hours = float(input("Study hours per week: "))
    attendance_rate = float(input("Attendance rate (0-100): "))
    quiz_score = float(input("Quiz score (0-100): "))
    exams_score = float(input("Midterm score (0-100): "))
    performance_task = float(input("Performance task score (0-100): "))
    activities = float(input("Activities score (0-50): "))

    X_new = np.array([[attendance_rate, quiz_score,
                       exams_score, performance_task, activities]])
    pred = model.predict(X_new)[0]
    print()
    print(f"Predicted final grade: {pred:.5f}")
    status = "PASS" if pred >= 76 else "FAIL"
    print(f"Predicted status: {status}")

