import sqlite3
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load your model from the DB
def load_student_data(db_name="students.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
        SELECT attendance_rate, quiz_score,
         exams_score, performance_task, activities, final_grade FROM students
    """)
    data = cur.fetchall()
    conn.close()
    X = np.array([row[:-1] for row in data])
    y = np.array([row[-1] for row in data])
    return X, y

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

# Predict for CSV rows
def predict_csv(model, csv_path, output_path):
    df = pd.read_csv(csv_path)

    # Fill missing activities column with 0 if not present
    if "activities" not in df.columns:
        df["activities"] = 0

    # Extract features in correct order
    X_new = df[[
        "attendance_rate",
        "Total_Quiz",
        "exams",
        "performance",
        "activities"
    ]].to_numpy()

    preds = model.predict(X_new)

    df["grade"] = preds

    df.to_csv(output_path, index=False)
    print(f"Saved updated CSV to {output_path}")


X, y = load_student_data()
model = train_model(X, y)
predict_csv(model, "grades.csv", "students_with_grades.csv")
