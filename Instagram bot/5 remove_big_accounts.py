import pandas as pd

file = "instagram_accounts.xlsx"

to_followers = 10
from_followers = 8000

accounts = pd.read_excel(file)
accounts['followers'] = accounts['followers'].apply(lambda x: str(x).replace(',',''))
accounts['followers'] = accounts['followers'].apply(lambda x: str(x).replace('K','000'))
accounts['followers'] = accounts['followers'].apply(lambda x: str(x).replace('M','000000'))
accounts = accounts[accounts['followers'] != "nan"]
accounts['followers'] = accounts['followers'].astype(int)
accounts = accounts[accounts['followers'] != 0]
accounts = accounts[(accounts['followers'] >= to_followers) & (accounts['followers'] <= from_followers)]
accounts.to_excel(file,index=False)