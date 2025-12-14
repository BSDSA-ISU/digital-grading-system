# main.py
import os
import sys
from utils.DataScience import ShowCourses as showbar
from utils.CRUD import setup_database, insert_student, delete_student, show_specific_student, ShowCol, update_student, find_students
from utils.PredictGrade import predict_db, predict_db_tabulate
DB_FILE = "student_grade.db"

def get_student_input():
    """Collect student data from user input."""

    return {
        "name": input("Student name: ").strip(),
        "student_id": input("Student ID: ").strip(),
        "program": input("Program: ").strip(),
        "grade": float(input("Raw grade: ")),
        "status": int(input("Status (1 = active, 0 = inactive): ")),
        "age": int(input("Age: ")),
        "attendance_rate": float(input("Attendance rate (0–100): ")),
        "quiz_score": float(input("Quiz score: ")),
        "exams_score": float(input("Exam score: ")),
        "performance_task": float(input("Performance task score: ")),
        "activities": float(input("Activities score (1 - 50): ")),
        "final_grade": float(input("Final grade: ")),
        "gpa": float(input("GPA: ")),
    }


def main():
    print(f"Initializing database: {DB_FILE}")
    conn = setup_database(DB_FILE)
    conn.close()

    while True:
        print("\nOptions:")
        print("1 - Insert new student")
        print("2 - Show all students")
        print("2.5 - show specific student")
        print("3 - Predict/compute from a database file")
        print("4 - update entriez")
        print("5 - show bar graph of courses")
        print("6 - Deleting")
        print("10 - exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            try:
                student_data = get_student_input()
                insert_student(DB_FILE, **student_data)
                print("Student record inserted.")
            except Exception as e:
                print(f"Failed to insert record: {e}")

        elif choice == "2":
            ShowCol(DB_FILE)

        elif choice == "2.5":
            partial_id = input("Enter partial student_id to search: ")
            find_students(student_id_partial=partial_id)

        elif choice == "3":
            predict_db_tabulate(db_path="student_grade.db", table_name="students", max_rows=999989)
        
        elif choice == "4":
            partial_id = input("Enter partial student_id to search: ")
            find_students(student_id_partial=partial_id)

            # Step 2: Pick which student to update
            student_id_to_update = input("Enter the full student_id of the student to update: ")

            # Step 3: Update fields
            # You can dynamically ask for fields to update or hardcode some for simplicity
            new_grade = float(input("Enter new grade: "))
            new_gpa = float(input("Enter new GPA: "))

            update_student(student_id=student_id_to_update, grade=new_grade, gpa=new_gpa)
        
        elif choice == "5":
            showbar()

        elif choice == "6":
            # Step 2: Pick which student to update
            student_id_to_delete = input("Enter the full student_id of the student to delete: ")

            delete_student(student_id_partial=student_id_to_delete)

        elif choice == "10":
            sys.exit(0)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
