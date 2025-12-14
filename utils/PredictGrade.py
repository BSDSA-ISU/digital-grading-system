import sqlite3
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from tabulate import tabulate

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

X, y = load_student_data()
pred = train_model(X, y)

# Predict for CSV rows
def predict_csv(csv_path, output_path, model=pred):
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

# for database sql
def predict_db(db_path, output_path="output.db", table_name="students", model=pred, output_table=None):
    output_table = output_table or table_name  # overwrite same table if not specified

    # Connect to DB
    with sqlite3.connect(db_path) as conn:
        # Read table into DataFrame
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

        # Fill missing column if needed
        if "activities" not in df.columns:
            df["activities"] = 0

        # Extract features
        X_new = df[[
            "attendance_rate",
            "Total_Quiz",
            "exams",
            "performance",
            "activities"
        ]].to_numpy()

        # Predict
        preds = model.predict(X_new)
        df["grade"] = preds

        # Save back to DB (overwrite table or create new one)
        df.to_sql(output_path, conn, if_exists="replace", index=False)
        print(f"Saved predictions to table '{output_table}' in {output_path}")

# show only
def predict_db_tabulate(db_path, model=pred,  table_name="students", max_rows=999989):
    # Connect to DB
    with sqlite3.connect(db_path) as conn:
        # Read table into DataFrame
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

        # Fill missing column if needed
        if "activities" not in df.columns:
            df["activities"] = 0

        # Extract features
        X_new = df[[
            "attendance_rate",
            "quiz_score",
            "exams_score",
            "performance_task",
            "activities"
        ]].to_numpy()

        # Predict
        df["grade"] = model.predict(X_new)

        # Reorder columns to put 'grade' at the end explicitly
        cols = [c for c in df.columns if c != "grade"] + ["grade"]
        df = df[cols]

        # Show first `max_rows` rows in a neat table
        print(tabulate(df.head(max_rows), headers="keys", tablefmt="grid"))

        choose = input("save the result as a new db file(y/n)?")
        if choose == "y":
            filename = input("type the filename(no need for file extension): ")
            conn = sqlite3.connect(f"{filename}.db")
            df.to_sql(f"{filename}.db", conn)