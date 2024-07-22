import requests
import os
import pandas as pd
from tqdm import tqdm

data = {
    "business_url": [],
}

keys = [
    {
        "API_KEY": "AIzaSyCbo2_EijloBabAIDnC4GmkBRaS_7gIoc0",
        "SEARCH_ENGINE_ID": "e6c90ee6e183b42a0",
    },
    {
        "API_KEY": "AIzaSyC5O3T2_VFqeAJ29dvgcJ9MOW4UNaXyQjc",
        "SEARCH_ENGINE_ID": "d758418e0c6ab49e3",
    },
    {
        "API_KEY": "AIzaSyAO6PNcyMGkhyN9jJCMz1_fI-MP_u_eG2Y",
        "SEARCH_ENGINE_ID": "d545ffd1860424fe9",
    },
]
files = os.listdir("new-sheets")

current_key_num = 0
key = keys[current_key_num]

queries = [
    """ site:instagram.com "Nails" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Manicure" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Nailart" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Acrylic" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Barbershop" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Spa" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Barber" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Grooming" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Haircut" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Shave" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Beard" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Plumbing" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Pipes" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Drain" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Water" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Repair" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Maintenance" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Roofer" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Leak" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Roofing" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Roof" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Contractor" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Replacement" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Inspection" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Carpet" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
    """ site:instagram.com "Trim" "100..8000 followers" -linktr.ee -bit.ly -lnk.bio -url.bio  """,
]

locations = [
    "USA",
    "UK",
    "Texas",
    "North Carolina",
    "California",
    "New York",
    "Los Angeles",
    "London",
    "Paris",
    "France",
    "Tokyo",

    
    "Japan",
    "Berlin",
    "Germany",
    "Miami",
    "Toronto",
    "Illinois",
    "Sydney",
    "Florida",
    "San Francisco",
]

new_queries = []

for location in locations:
    for query in queries:
        new_query = f""" {query} "{location}" """
        new_queries.append(new_query)

def search_instagram_accounts(api_key, search_engine_id, queries):
    global current_key_num

    instagram_accounts = []
    instagram_accounts_count = 0

    for query in tqdm(queries):
        instagram_accounts_count += 1
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": api_key,
            "cx": search_engine_id,
            "q": query,
            "num": 10,  # Increased number of results per query
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()

            for item in results.get("items", []):
                data["business_url"].append(item["link"])

            df = pd.DataFrame(data)
            df.to_excel(
                f"new-sheets/instagram_accounts-{len(files)+1}.xlsx", index=False
            )

        elif response.status_code == 429:
            current_key_num = (current_key_num + 1) % len(
                keys
            )  # Move to the next key in circular manner
            print(f"Switching to key {current_key_num}")
            print(f"Total Accounts Found ({instagram_accounts_count})")
            return search_instagram_accounts(
                keys[current_key_num]["API_KEY"],
                keys[current_key_num]["SEARCH_ENGINE_ID"],
                queries,
            )

        else:
            print(query)
            print(response.status_code)


search_instagram_accounts(key["API_KEY"], key["SEARCH_ENGINE_ID"], new_queries)
