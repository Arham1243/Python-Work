import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# List of URLs
urls = [
    "https://html.dynamiclayers.net/dl/barbershop/",
]


# Function to extract image paths from a webpage
def extract_image_paths(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        img_tags = soup.find_all("img")
        img_paths = [img["src"] for img in img_tags if "src" in img.attrs]
        print(f"images Found: {len(img_paths)}  Url: {url}")
        return img_paths
    except Exception as e:
        print(f"{url}: {e}")
        return []


# Writing image paths to a file
unique_paths = set()
for url in urls:
    image_paths = extract_image_paths(url)
    folder_name = url.split("/")[-1]
    for path in image_paths:
        unique_paths.add(f"{folder_name}/{path}")

with open("image_paths.py", "a") as f:
    f.write(str(unique_paths))
