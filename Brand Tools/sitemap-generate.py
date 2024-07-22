import sys
import logging
import asyncio
from flask import Flask, request, jsonify
from pysitemap import crawler
from pysitemap.parsers.lxml_parser import Parser

app = Flask(__name__)

files_to_ignore = [
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".tif", ".tiff",
    ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp",
]

def generate_sitemap(url):
    folder_name  = url.split("://")[1].replace("/", "")
    save_path = f"{folder_name}/sitemap.xml"
    root_url = url
    exclude_media_extensions = files_to_ignore
    exclude_urls = [ext for ext in exclude_media_extensions]

    asyncio.set_event_loop(asyncio.new_event_loop())  # Set up a new event loop for each thread

    crawler(
        root_url,
        out_file=save_path,
        exclude_urls=exclude_urls,
        http_request_options={"ssl": False},
        parser=Parser,
    )

@app.route('/api/sitemap')
def get_sitemap():
    url = request.args.get('url')
    folder_name  = url.split("://")[1].replace("/", "")
    if not url:
        return jsonify({"error": "URL parameter is missing"}), 400

    generate_sitemap(url)
    with open(f"{folder_name}/sitemap.xml", "r") as file:
        sitemap_content = file.read()
    return sitemap_content, 200

if __name__ == "__main__":
    app.run(debug=True)

# aiohttp
# asyncio
# aiofile

# lxml
# cssselect