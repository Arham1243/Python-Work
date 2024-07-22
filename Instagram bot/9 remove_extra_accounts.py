import pandas as pd

file = "send_dm.xlsx"

def remove_nos(file):
    df = pd.read_excel(file)
    df = df[df["target"] != "No"]
    df.to_excel(file, index=False)

remove_nos(file)