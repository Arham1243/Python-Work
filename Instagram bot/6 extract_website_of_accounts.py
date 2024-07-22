from time import sleep
from bs4 import BeautifulSoup
import re
import webbrowser
import pyautogui
import requests
from tqdm import tqdm
import pyperclip
import pandas as pd

file = "instagram_accounts.xlsx"
df = pd.read_excel(file)


link = "https://www.instagram.com/"

if "status_code" in df.columns and "website" in df.columns:
    df["status_code"] = df["status_code"].fillna("")
    untouched_df = df[df["website"].isna()]
    handles = untouched_df["handle"]
else:
    handles = df["handle"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://www.google.com/",
}


def update_sheet(handle, website, status_code):
    try:
        if website and "facebook.com" in website.lower():
            website = "no"
            status_code = 404

        df.loc[df["handle"] == handle, ["website", "status_code", "links"]] = [
            "yes" if website else "no",
            status_code,
            website,
        ]

        print(f"Website: {website if website else 'no'}, Status Code: {status_code}")
        df.to_excel(file, index=False)
        print("Sheet Updated")

    except Exception as e:
        print(f"Error updating sheet for handle {handle}: {e}")


def check_urls(urls):
    working_urls = []
    status_codes = []
    for url in urls:
        try:
            formatted_url = url.strip()
            if not formatted_url.startswith("http://") and not formatted_url.startswith(
                "https://"
            ):
                formatted_url = "https://" + formatted_url.lstrip("www.")
            response = requests.get(formatted_url, headers=headers)
            status_codes.append(response.status_code)
            print(response.status_code, formatted_url)
            if response.status_code == 200:
                working_urls.append(url)
        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")
            status_codes.append(str(e))
    return working_urls, status_codes


def detect_urls(input_list):
    url_pattern = re.compile(
        r"\b(?:https?://|www\.|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})[a-zA-Z0-9./?=&-]*\b"
    )
    detected_urls = []
    for item in input_list:
        if isinstance(item, str):
            matches = url_pattern.findall(item)
            if matches:
                detected_urls.extend(matches)
    urls, status_codes = check_urls(detected_urls)
    print(urls)
    if urls:
        return ", ".join(urls), status_codes[0] if status_codes else "No status code"
    else:
        return None, status_codes[0] if status_codes else "No URL detected"


def execute_script():
    try:
        pyautogui.hotkey("ctrl", "shift", "j")
        sleep(5)
        script = """const htmlContent = document.querySelector("section.xc3tme8.x1uhmqq1.x1xdureb.xo55r9g.x1vnunu7.x14tfgiu.xlrpkbc.xpoid6y.x16zxmhm.x6ikm8r.x10wlt62").innerHTML; const textarea = document.createElement('textarea'); textarea.value = htmlContent; document.body.appendChild(textarea); textarea.select(); textarea.setSelectionRange(0, 99999); document.execCommand('copy'); document.body.removeChild(textarea);"""
        pyautogui.write(script, interval=0.01)
        pyautogui.hotkey("enter")
    except Exception as e:
        print(f"Error executing script: {e}")


def get_details(handle):
    try:
        ig_link = f"{link}{handle}"
        pyautogui.hotkey("ctrl", "w")
        sleep(1)
        webbrowser.open(ig_link)
        sleep(8)
        execute_script()
    except Exception as e:
        print(f"Error opening Instagram handle {handle}: {e}")


def get_details_from_html(handle):
    try:
        html_content = pyperclip.paste()
        soup = BeautifulSoup(html_content, "html.parser")
        text_content = soup.get_text(separator="\n")
        bio_texts = text_content.split()
        url_text, status_code = detect_urls(bio_texts)
        if url_text:
            update_sheet(handle, url_text, status_code)
        else:
            update_sheet(handle, None, status_code)
    except Exception as e:
        print(f"Error getting details from HTML for handle {handle}: {e}")
        update_sheet(handle, None, "Error processing HTML")


for handle in tqdm(handles):
    get_details(handle)
    get_details_from_html(handle)
