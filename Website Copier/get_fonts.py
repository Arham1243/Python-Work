import os
import requests


def download_and_save_font(url, folder_path, headers=None):
    # Get the file name from the URL
    file_name = os.path.join(folder_path, os.path.basename(url.split("?")[0]))

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
    # URL list for font files
    font_urls = [
    
"https://html.dynamiclayers.net/dl/barbershop/fonts/ElegantIcons.woff",
"https://html.dynamiclayers.net/dl/barbershop/fonts/barber-icon.ttf?pkr5cj",
"https://html.dynamiclayers.net/dl/barbershop/fonts/ElegantIcons.ttf",
"https://html.dynamiclayers.net/dl/barbershop/fonts/ElegantIcons.woff",
"https://html.dynamiclayers.net/dl/barbershop/fonts/barber-icon.woff?pkr5cj",
    ]

    # Folder path to save font files
    font_folder = "assets/fonts"

    # Create the folder if it doesn't exist
    if not os.path.exists(font_folder):
        os.makedirs(font_folder)

    # Additional headers to make the request more legitimate
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Download and save each font file
    for font_url in font_urls:
        download_and_save_font(font_url, font_folder, headers=headers)
