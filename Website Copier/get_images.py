import requests
import os
from urllib.parse import urlparse, unquote


def get_relative_path_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    # Unquoting the path to handle special characters in the URL
    decoded_path = unquote(path)
    # Remove leading and trailing slashes
    cleaned_path = decoded_path.strip("/")
    return cleaned_path


def download_images(image_links, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for idx, image_link in enumerate(image_links, start=1):
        try:
            response = requests.get(image_link)
            response.raise_for_status()

            # Get relative path from URL
            relative_path = get_relative_path_from_url(image_link)
            # Create directories if they don't exist
            relative_path_parts = relative_path.split("/")
            # Ensure that directories are created as needed
            for i in range(len(relative_path_parts) - 1):
                output_path = os.path.join(output_folder, *relative_path_parts[: i + 1])
                os.makedirs(output_path, exist_ok=True)

            # Get filename from URL
            filename = os.path.basename(urlparse(image_link).path)
            # Add index to filename to avoid duplicates
            filename = f"{idx}_{filename}"

            with open(os.path.join(output_folder, relative_path), "wb") as f:
                f.write(response.content)

            print(f"Image {idx} downloaded successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image {idx}: {e}")


if __name__ == "__main__":
    image_links = [
        "https://html.dynamiclayers.net/dl/barbershop/img/about-3.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/post-1.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/post-3.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/about-1.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/loading.gif",
        "https://html.dynamiclayers.net/dl/barbershop/img/sponsor-2.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/team-2.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/sponsor-3.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/team-1.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/about-logo.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/team-3.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/team-4.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/sponsor-1.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/sponsor-5.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/sponsor-4.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/about-2.jpg",
        "https://html.dynamiclayers.net/dl/barbershop/img/logo.png",
        "https://html.dynamiclayers.net/dl/barbershop/img/post-2.jpg",
    ]

    output_folder = "assets"

    download_images(image_links, output_folder)
