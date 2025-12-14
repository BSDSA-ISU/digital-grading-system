import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

folder_path = "./"
os.makedirs(folder_path, exist_ok=True)

# Persistent database path
db_path = folder_path + "/infirmary.db"

# Connect to database permanently saved in Drive
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients (
    PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID TEXT UNIQUE,
    Name TEXT,
    Age INTEGER,
    Gender TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cases (
    CaseID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    VisitDate TEXT,
    Diagnosis TEXT,
    Symptoms TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
)
""")

conn.commit()

# ADD STUDENT
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender (M/F): ")

    try:
        cursor.execute("""
            INSERT INTO Patients (StudentID, Name, Age, Gender)
            VALUES (?, ?, ?, ?)
        """, (sid, name, age, gender))
        conn.commit()
        print("Student added successfully!\n")
    except:
        print("Error: Student ID may already exist.\n")


# ADD CASE
def add_case():
    student_id = input("Enter Student ID: ")

    cursor.execute("SELECT PatientID FROM Patients WHERE StudentID=?", (student_id,))
    result = cursor.fetchone()

    if not result:
        print("Student not found.\n")
        return

    patient_id = result[0]

    date = input("Enter Visit Date (YYYY-MM-DD): ")
    diagnosis = input("Enter Diagnosis: ")
    symptoms = input("Enter Symptoms: ")

    cursor.execute("""
        INSERT INTO Cases (PatientID, VisitDate, Diagnosis, Symptoms)
        VALUES (?, ?, ?, ?)
    """, (patient_id, date, diagnosis, symptoms))

    conn.commit()
    print("Case added successfully!\n")


# VIEW ALL CASES
def view_all_cases():
    df = pd.read_sql_query("""
        SELECT Cases.CaseID, Patients.Name, Cases.VisitDate, Cases.Diagnosis
        FROM Cases
        JOIN Patients ON Cases.PatientID = Patients.PatientID
    """, conn)

    if df.empty:
        print("No cases found.\n")
    else:
        print(df.to_string(index=False))

    print()


# UPDATE CASE
def update_case():
    case_id = input("Enter Case ID to update: ")

    new_diagnosis = input("New Diagnosis: ")
    new_symptoms = input("New Symptoms: ")

    cursor.execute("""
        UPDATE Cases
        SET Diagnosis=?, Symptoms=?
        WHERE CaseID=?
    """, (new_diagnosis, new_symptoms, case_id))

    conn.commit()
    print("Case updated successfully!\n")


# DELETE CASE
def delete_case():
    case_id = input("Enter Case ID to delete: ")

    cursor.execute("DELETE FROM Cases WHERE CaseID=?", (case_id,))
    conn.commit()
    print("Case deleted successfully!\n")


# DELETE ALL CASES
def delete_all_cases():
    confirm = input("Are you sure you want to delete ALL cases? (yes/no): ")

    if confirm.lower() == "yes":
        cursor.execute("DELETE FROM Cases")
        conn.commit()
        print("All cases deleted successfully!\n")
    else:
        print("Operation cancelled.\n")


# DELETE STUDENT + THEIR CASES
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    cursor.execute("SELECT PatientID FROM Patients WHERE StudentID=?", (student_id,))
    result = cursor.fetchone()

    if not result:
        print("Student not found.\n")
        return

    patient_id = result[0]

    cursor.execute("DELETE FROM Cases WHERE PatientID=?", (patient_id,))
    cursor.execute("DELETE FROM Patients WHERE PatientID=?", (patient_id,))
    conn.commit()

    print("Student and all related cases deleted successfully!\n")


# DESCRIPTIVE STATISTICS
def descriptive_stats():
    df = pd.read_sql_query("SELECT * FROM Cases", conn)

    if df.empty:
        print("No data available.\n")
        return

    total_cases = len(df)
    most_common = df["Diagnosis"].value_counts().idxmax()
    weekly_avg = total_cases / 4

    print(f"Total Cases: {total_cases}")
    print(f"Most Common Diagnosis: {most_common}")
    print(f"Average Cases Per Week: {weekly_avg:.1f}\n")

    df["Diagnosis"].value_counts().plot(kind="bar")
    plt.title("Most Common Diagnoses")
    plt.xlabel("Diagnosis")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


# WEEKLY TREND ANALYSIS
def weekly_trend():
    df = pd.read_sql_query("SELECT VisitDate FROM Cases", conn)

    if df.empty:
        print("No data available.\n")
        return

    df["VisitDate"] = pd.to_datetime(df["VisitDate"])
    df["Week"] = df["VisitDate"].dt.isocalendar().week

    weekly_count = df.groupby("Week").size()

    print("Weekly Sickness Count:")
    print(weekly_count)

    weekly_count.plot(kind="line", marker="o")
    plt.title("Weekly Sickness Trend")
    plt.xlabel("Week Number")
    plt.ylabel("Number of Cases")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("\nINFIRMARY SYSTEM ")
        print("1. Add Student")
        print("2. Add Case")
        print("3. View All Cases")
        print("4. Update Case")
        print("5. Delete Case")
        print("6. Delete All Cases")
        print("7. Delete Student + All Their Cases")
        print("8. Descriptive Statistics")
        print("9. Weekly Trend Analysis")
        print("10. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_case()
        elif choice == "3":
            view_all_cases()
        elif choice == "4":
            update_case()
        elif choice == "5":
            delete_case()
        elif choice == "6":
            delete_all_cases()
        elif choice == "7":
            delete_student()
        elif choice == "8":
            descriptive_stats()
        elif choice == "9":
            weekly_trend()
        elif choice == "10":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

try:
    main()
finally:
    if conn:
        conn.close()
        print("Database connection closed.")
