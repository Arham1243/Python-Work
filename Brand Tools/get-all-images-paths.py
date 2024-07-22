import requests
from bs4 import BeautifulSoup

# List of URLs
urls = [
    "https://amazonpublishingpros.co",
    "https://amazonpublishingpros.co/ebook-writing-publishing",
    "https://amazonpublishingpros.co/audio-book-service",
    "https://amazonpublishingpros.co/book-editing-proofreading",
    "https://amazonpublishingpros.co/book-cover-design",
    "https://amazonpublishingpros.co/book-illustration",
    "https://amazonpublishingpros.co/book-publishing",
    "https://amazonpublishingpros.co/book-printing",
    "https://amazonpublishingpros.co/book-marketing",
    "https://amazonpublishingpros.co/author-website",
    "https://amazonpublishingpros.co/amazon-publishing-service",
    "https://amazonpublishingpros.co/contact-us",
    "https://amazonpublishingpros.co/privacy-policy",
    "https://amazonpublishingpros.co/terms-and-conditions"
]

# Function to extract image sources from a URL
def extract_image_sources(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        image_sources = [img['data-src'] for img in img_tags if 'data-src' in img.attrs]
        return image_sources
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return []

# Iterate through each URL and print image sources
for url in urls:
    # print(f"\nImage sources for {url}:\n")
    image_sources = extract_image_sources(url)
    for src in image_sources:
        print(src)
