import os
import requests


def download_and_save_css(url, folder_path, headers=None):
    # Get the file name from the URL
    file_name = os.path.join(folder_path, url.split("/")[-1])

    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the content to a file
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"{file_name} saved successfully.")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")


if __name__ == "__main__":
    # URL list
    css_urls = [
        "https://html.dynamiclayers.net/dl/barbershop/css/venobox/venobox.css",
    ]

    # Folder path to save CSS files
    css_folder = "assets/css"

    # Create the folder if it doesn't exist
    if not os.path.exists(css_folder):
        os.makedirs(css_folder)

    # Additional headers to make the request more legitimate
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Download and save each CSS file
    for css_url in css_urls:
        download_and_save_css(css_url, css_folder, headers=headers)
