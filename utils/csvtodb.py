import pandas as pd
import sqlite3

def csvtodb(csv_path, filepath : str):

    conn = sqlite3.connect(filepath)

    df = pd.read_csv(csv_path)

    df.to_sql(filepath, conn)

csvtodb("grades.csv", "g.pd")