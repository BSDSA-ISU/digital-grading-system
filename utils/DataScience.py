import sqlite3
from matplotlib.pyplot import plot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def LinearRegressions():

    conn = sqlite3.connect("students.db")
    df = pd.read_sql_query("SELECT final_score, gpa FROM students", conn)
    conn.close()

    X = df[['final_score']]  # independent variable (2D array)
    Y = df['gpa']            # dependent variable

    model = LinearRegression()
    model.fit(X, Y)

    Y_pred = model.predict(X)

    r2 = r2_score(Y, Y_pred)
    print(f"Linear regression model: GPA = {model.coef_[0]:.3f}*FinalScore + {model.intercept_:.3f}")
    print(f"R-squared: {r2:.3f}")

    plt.scatter(X, Y, color='blue', label='Actual GPA')
    plt.plot(X, Y_pred, color='red', linewidth=2, label='Regression Line')
    plt.xlabel("Final Exam Score")
    plt.ylabel("GPA (1 = highest)")
    plt.title("Linear Regression: Final Score → GPA")
    plt.legend()
    plt.show()


def age_mean():
    con = sqlite3.connect("students.db")
    cursor = con.cursor()

    cursor.execute("select * from students;")
    x= cursor.fetchall()

    cursor.close()

    age = []

    for i in x:
        age.append(i[5])

    return sum(age) / len(age)

def AgeBar():
    plt.bar([1], [M], color="green", label=f"Male ({M})")
    plt.bar([2], [F], color="pink", label=f"Female ({F})")
    plt.legend()
    plt.show()
    plt.clf()

LinearRegressions()
