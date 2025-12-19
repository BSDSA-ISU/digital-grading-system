import sqlite3
import pandas as pd

def convert_to_csv(db_file="student_grade.db", csv_file="student_grade.csv"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_sql("SELECT * FROM students", conn)
        df.to_csv(csv_file, index=False)
        print(f"CSV export successful and saved as {csv_file}.")
    except Exception as e:
        print("Export failed:", e)
    finally:
        if conn:
            conn.close()
