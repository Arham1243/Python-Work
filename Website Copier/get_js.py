import os
import requests


def download_and_save_file(url, folder_path, headers=None):
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
    # URL list for JS files
    js_urls = [
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/modernizr-2.8.3-respond-1.4.2.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/jquery-1.12.4.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/bootstrap.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/imagesloaded.pkgd.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/owl.carousel.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/jquery.isotope.v3.0.2.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/smooth-scroll.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/venobox.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/jquery.ajaxchimp.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/jquery.slicknav.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/jquery.nice-select.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/jquery.mb.YTPlayer.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/vendor/wow.min.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/contact.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/appointment.js",
        "https://html.dynamiclayers.net/dl/barbershop/js/main.js",
    ]

    # Folder path to save JS files
    js_folder = "assets/js"

    # Create the folder if it doesn't exist
    if not os.path.exists(js_folder):
        os.makedirs(js_folder)

    # Additional headers to make the request more legitimate
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Download and save each JS file
    for js_url in js_urls:
        download_and_save_file(js_url, js_folder, headers=headers)
