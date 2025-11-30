import sqlite3
from matplotlib.pyplot import plot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import Lasso
import seaborn as sns

def LogisticRegressionTable():
    # Connect to your database
    conn = sqlite3.connect("students.db")

    # Load data from SQLite
    df = pd.read_sql_query("SELECT final_score, midterm_score, quiz_score, status FROM students", conn)

    X = df[['final_score', 'midterm_score', 'quiz_score']]
    Y = df['status']   # 1 = passed, 0 = failed

    # Train model
    model = LogisticRegression()
    model.fit(X, Y)

    # Predict pass/fail probability
    df['pass_prob'] = model.predict_proba(X)[:, 1]
    df['pass_prob'] = df['pass_prob'].round(4)

    # Convert to final 0/1
    #df['pass_pred'] = (df['pass_prob'] >= 0.5).astype(int)

    df['pass_pred'] = model.predict(X)

    print(df)

    model.fit(X[Y.notnull()], Y[Y.notnull()])

    # Y_pred = model.predict(X)

 #   r2 = r2_score(Y, Y_pred)
  #  print(f"R-squared: {r2}")


    # Predict someone
    zero_student = pd.DataFrame([{
        'final_score': 33,
        'midterm_score': 49,
        'quiz_score': 49
    }])

    prob = model.predict_proba(zero_student)[0][1]
    pred = model.predict(zero_student)[0]

    print("Zero student pass probability:", round(prob, 3))
    print("Prediction (1=Pass, 0=Fail):", pred)

def total_exams_score():
    conn = sqlite3.connect("./students.db")
    df = pd.read_sql_query("SELECT final_grade FROM students", conn)

    plt.hist(df['final_grade'], bins=100, color='skyblue', edgecolor='black')
    plt.title("Final Grade Distribution")
    plt.xlabel("Final Grade")
    plt.ylabel("Number of Students")
    plt.xticks(range(10, 101, 10))
    plt.show()


def LinTest(db_name="students.db"):
    # Load dataset
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT age, gpa, status, attendance_rate, quiz_score, exams_score, performance_task, activities, final_grade FROM students", conn)

    # Features and target
    X = df[['quiz_score', 'attendance_rate', 'exams_score', 'performance_task', 'activities']]
    y = df['final_grade']

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # R^2 score
    r2 = r2_score(y_test, y_pred)
    print(f"R²: {r2:.4f}")

    # Plot actual vs predicted
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([50, 100], [50, 100], 'r--')  # perfect fit line
    plt.xlabel("Actual Final Grade")
    plt.ylabel("Predicted Final Grade")
    plt.title("Linear Regression: Actual vs Predicted Final Grade")
    plt.grid(True)
    plt.show()

def lassso(db_name="students.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT grade, gpa, attendance_rate, status, quiz_score, exams_score, performance_task, activities, final_grade FROM students", conn)

    predicters = ['quiz_score', 'exams_score', 'attendance_rate', 'performance_task', 'activities']

    # Features and target
    X = df[predicters]
    y = df['final_grade']

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    lasso = Lasso(alpha=0.1)  # adjust alpha if too many/few features remain
    lasso.fit(X_train, y_train)

    # Predict
    y_pred = lasso.predict(X_test)

    # Evaluation
    print("R²:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))

    selected_features = pd.Series(lasso.coef_, index=predicters)
    selected_features = selected_features[selected_features != 0].sort_values(key=abs, ascending=False)
    print("\nSelected features and coefficients:\n", selected_features)

# Run test
if __name__ == "__main__":
    total_exams_score()
    LinTest()
    lassso()