import pandas as pd

file = "instagram_accounts.xlsx"
df = pd.read_excel(file)
df = df[df["status_code"] != 200]

df = df[df["website"] == "no"]
df["status_code"] = df["status_code"].astype(str)
df.loc[df["status_code"].str.contains("HTTPSConnectionPool"), "status_code"] = "408"
df.loc[df["status_code"].str.contains("Connection aborted"), "status_code"] = "408"
df.loc[df["status_code"].str.contains("No URL detected"), "status_code"] = "404"
df = df[df["status_code"] == "404"]
df.to_excel("send_dm.xlsx", index=False)
