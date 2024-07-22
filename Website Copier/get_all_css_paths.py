import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# List of URLs
urls = [
    "https://amazonkindleofficial.com",
    "https://amazonkindleofficial.com/service.php",
    "https://amazonkindleofficial.com/editing",
    "https://amazonkindleofficial.com/ghost-writing-services",
    "https://amazonkindleofficial.com/book-publishing",
    "https://amazonkindleofficial.com/audio-book.php",
    "https://amazonkindleofficial.com/book-printing-services.php",
    "https://amazonkindleofficial.com/bookcover",
    "https://amazonkindleofficial.com/childrens-book",
    "https://amazonkindleofficial.com/book-marketing",
    "https://amazonkindleofficial.com/about.php",
    "https://amazonkindleofficial.com/testimonials.php",
    "https://amazonkindleofficial.com/contact.php",
    "https://amazonkindleofficial.com/privacy.php",
    "https://amazonkindleofficial.com/term-conditions.php",
    "https://amazonkindleofficial.com/refund-policy.php",
]


# Function to extract image paths from a webpage
def extract_image_paths(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        css_links = soup.find_all("link", rel="stylesheet")
        css_links_paths = [link.get("href") for link in css_links]
        print(f"Links Found: {len(css_links_paths)}  Url: {url}")
        return css_links_paths
    except Exception as e:
        print(f"{url}: {e}")
        return []


# Writing image paths to a file
unique_paths = set()
for url in urls:
    image_paths = extract_image_paths(url)
    for path in image_paths:
        unique_paths.add(path)

with open("css_link.py", "a") as f:
    f.write(str(unique_paths))
