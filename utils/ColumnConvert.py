import pandas as pd

def quiz_percentage(df, col_name="quiz_percentage"):
    quizzes = df.filter(regex=r"(?i)quiz")

    if quizzes.empty:
        return df.assign(**{col_name: 0})

    totals = quizzes.sum(axis=1)
    max_total = totals.max() or 1

    return df.assign(**{
        col_name: totals / max_total * 100
    })


text = pd.read_csv("./grades.csv")

result = quiz_percentage(text)
print(result)