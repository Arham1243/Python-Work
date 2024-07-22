import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_instagram_followers(handle):
    url = f"https://www.instagram.com/{handle}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        meta_tag = soup.find("meta", property="og:description")
        if meta_tag:
            description = meta_tag["content"]
            followers = description.split(" ")[0]
            return followers
    return None



# Load the Excel file
file_path = "instagram_accounts.xlsx"
df = pd.read_excel(file_path)

# Ensure the 'handle' column exists
if "handle" in df.columns:
    for idx, handle in tqdm(df["handle"].items(), total=len(df)):
        # Get followers count for each handle and store it in the DataFrame
        followers = get_instagram_followers(handle)
        df.loc[idx, "followers"] = followers
        df.to_excel(file_path, index=False)
    print("Updated Excel file with followers count.")
else:
    print("'handle' column not found in the Excel file.")
