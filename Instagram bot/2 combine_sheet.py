import pandas as pd
import os

files = os.listdir('new-sheets')
dfs = []

for file in files:
    df = pd.read_excel(f"new-sheets/{file}")
    dfs.append(df)
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_excel("instagram_accounts.xlsx",index=False)