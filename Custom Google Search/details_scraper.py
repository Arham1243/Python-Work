import pandas as pd
from time import sleep
import os
from tqdm import tqdm
from instagrapi import Client

# Initialize Instagrapi client
client = Client()

# Login to Instagram
client.login(username="ashnakhn_14", password="lucifer123")

# Function to scrape Instagram page and save HTML
def get_ig_details(handle):

  

    # Get user details (replace 'target_username' with the username of the user you want to fetch details for)
    user = client.user_info_by_username(handle)

    client.logout()
    return user


folder_name = "barbershop"
files = os.listdir("barbershop")
for file in files:
    try:
        data = pd.read_excel(f"{folder_name}/{file}")
        df = pd.DataFrame(data)
        df["followers"] = None
        df["website"] = None
        df["number"] = None
        df["email"] = None
        urls = df["business_url"]

        for url in tqdm(urls):
            target_url = url
            handle = url.split("https://www.instagram.com/")[1].split("/")[0]

            user = get_ig_details(handle)
            links = []
            for bio_link in user.bio_links:
                if bio_link.url:
                    links.append(bio_link.url)
                elif bio_link.lynx_url:
                    links.append(bio_link.lynx_url)

            number = user.contact_phone_number
            email = user.public_email
            followers = user.follower_count

            df.loc[df["business_url"] == target_url, "followers"] = followers
            df.loc[df["business_url"] == target_url, "email"] = email
            df.loc[df["business_url"] == target_url, "number"] = number
            df.loc[df["business_url"] == target_url, "website"] = links

        df.to_excel(f"new-updated/{file}", index=False)
    except Exception as e:
        print(e)
