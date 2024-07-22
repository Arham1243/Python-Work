import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse


def is_image_url(css_url, url):
    full_url = urljoin(css_url, url.strip('\'"'))
    _, file_extension = os.path.splitext(full_url.lower())
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']  # Add more if needed

    return file_extension in image_extensions


def download_image(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the filename from the URL
        filename = os.path.basename(urlparse(url).path)
        # Create directories based on the folder structure in the URL
        folder_structure = os.path.dirname(urlparse(url).path)
        full_folder_path = os.path.join(folder_path, folder_structure)
        os.makedirs(full_folder_path, exist_ok=True)
        # Save the image to the relevant folder
        filepath = os.path.join(full_folder_path, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filepath}")
    else:
        print(f"Failed to download: {url}")


def get_css_images(css_url, folder_path, headers=None):
    # Fetch CSS content
    response = requests.get(css_url, headers=headers)
    css_content = response.text

    # Use regex to find URLs in CSS content
    image_urls = re.findall(r'url\((.*?)\)', css_content)

    for url in image_urls:
        # Combine relative URLs with the base URL of the CSS file
        full_url = urljoin(css_url, url.strip('\'"'))
        if is_image_url(css_url, full_url):
            # Download the image to the specified folder
            download_image(full_url, folder_path)


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    css_url = "https://amazonkindleofficial.com/assets/css/custom.css?v1"
    folder_path = "assets/images"

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    get_css_images(css_url, folder_path, headers)
