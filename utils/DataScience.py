import sqlite3
from matplotlib.pyplot import plot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score

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

LogisticRegressionTable()
