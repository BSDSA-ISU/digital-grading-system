import sqlite3
from matplotlib.pyplot import plot as plt

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