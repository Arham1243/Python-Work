import requests
import os
import pandas as pd

data = {
    "business_url": [],
}

files = os.listdir("others")


def search_instagram_accounts(api_key, search_engine_id, queries):
    instagram_accounts = []

    for query in queries:
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
                data["business_name"].append(item["title"])
                data["business_desc"].append(item["snippet"])
                data["business_url"].append(item["link"])
                print(item["title"])
            df = pd.DataFrame(data)

            df.to_excel(f"others/instagram_accounts-{len(files)+1}.xlsx", index=False)
        else:
            print(query)
            print(response.status_code)


# API_KEY = "AIzaSyDX_kUuciDwldnySGVfMlLNvrQP8KzuHmo"
# SEARCH_ENGINE_ID = "007f376a27ff847d3"

# API_KEY = "AIzaSyCbo2_EijloBabAIDnC4GmkBRaS_7gIoc0"
# SEARCH_ENGINE_ID = "e6c90ee6e183b42a0"

# API_KEY = "AIzaSyC5O3T2_VFqeAJ29dvgcJ9MOW4UNaXyQjc"
# SEARCH_ENGINE_ID = "d758418e0c6ab49e3"

API_KEY = "AIzaSyAO6PNcyMGkhyN9jJCMz1_fI-MP_u_eG2Y"
SEARCH_ENGINE_ID = "d545ffd1860424fe9"

queries = [
    "site:instagram.com 'Plumbing service' '1000..5000 followers'",
    "site:instagram.com 'Plumbing repair' '1000..5000 followers'",
    "site:instagram.com 'Emergency plumber' '1000..5000 followers'",
    "site:instagram.com 'Residential plumber' '1000..5000 followers'",
    "site:instagram.com 'Commercial plumber' '1000..5000 followers'",
    "site:instagram.com 'Home remodeling' '1000..5000 followers'",
    "site:instagram.com 'Kitchen remodeling' '1000..5000 followers'",
    "site:instagram.com 'Bathroom remodeling' '1000..5000 followers'",
    "site:instagram.com 'Remodeling contractor' '1000..5000 followers'",
    "site:instagram.com 'Residential remodeling' '1000..5000 followers'",
    "site:instagram.com 'Roofing service' '1000..5000 followers'",
    "site:instagram.com 'Roof repair' '1000..5000 followers'",
    "site:instagram.com 'Roof installation' '1000..5000 followers'",
    "site:instagram.com 'Residential roofing' '1000..5000 followers'",
    "site:instagram.com 'Commercial roofing' '1000..5000 followers'",
    "site:instagram.com 'House cleaning service' '1000..5000 followers'",
    "site:instagram.com 'Residential cleaning' '1000..5000 followers'",
    "site:instagram.com 'Home cleaning' '1000..5000 followers'",
    "site:instagram.com 'Maid service' '1000..5000 followers'",
    "site:instagram.com 'Deep cleaning service' '1000..5000 followers'",
    "site:instagram.com 'Carpet cleaning service' '1000..5000 followers'",
    "site:instagram.com 'Residential carpet cleaning' '1000..5000 followers'",
    "site:instagram.com 'Commercial carpet cleaning' '1000..5000 followers'",
    "site:instagram.com 'Steam carpet cleaning' '1000..5000 followers'",
    "site:instagram.com 'Rug cleaning service' '1000..5000 followers'",
    "site:instagram.com 'Pressure washing service' '1000..5000 followers'",
    "site:instagram.com 'Power washing' '1000..5000 followers'",
    "site:instagram.com 'Residential pressure washing' '1000..5000 followers'",
    "site:instagram.com 'Deck pressure washing' '1000..5000 followers'",
]


locations = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Philadelphia",
    "Dallas",
    "San Jose",
    "San Diego",
    "Phoenix",
    "San Antonio",
    "London",
    "Manchester",
    "Birmingham",
    "Glasgow",
    "Edinburgh",
    "Toronto",
    "Vancouver",
    "Montreal",
    "Calgary",
    "Ottawa",
    "Sydney",
    "Melbourne",
    "Brisbane",
    "Perth",
    "Adelaide",
    "Berlin",
    "Munich",
    "Hamburg",
    "Cologne",
    "Frankfurt",
    "Paris",
    "Marseille",
    "Lyon",
    "Toulouse",
    "Nice",
]

new_queries = []


for location in locations:
    for query in queries:
        new_queries.append(f"{query} '{location}'")

# Perform the search
instagram_accounts = search_instagram_accounts(API_KEY, SEARCH_ENGINE_ID, new_queries)
