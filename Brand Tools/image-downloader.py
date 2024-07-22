import requests
import os
from urllib.parse import urlparse

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"


def get_filename_from_url(url):
    parsed_url = urlparse(url)
    return os.path.basename(parsed_url.path)


def download_images(image_links, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    headers = {"User-Agent": USER_AGENT}
    for idx, image_link in enumerate(image_links, start=1):
        try:
            response = requests.get(image_link, headers=headers)
            response.raise_for_status()

            filename = os.path.join(output_folder, get_filename_from_url(image_link))

            with open(filename, "wb") as f:
                f.write(response.content)

            print(f"Image {idx} downloaded ✅")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image {idx}: {e}")


if __name__ == "__main__":
    image_links = [
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/paypal_border.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/visa.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/mastercard.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/jcb.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/amex.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/sofort.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/discover.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/googlepay.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/klarna.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/bancontact.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/applepay.svg",
        "https://cdn.getyourguide.com/tf/assets/static/payment-methods/maestro.svg",
    ]

    output_folder = "images"

    download_images(image_links, output_folder)
