import json
import requests
import os

details = [
    {"username": "JAMESJOHNSON", "License API": "BC62CFD5-6DCC-45F9-B24D-20D1DBBE3D4F"},
    {"username": "JAMESBROWN", "License API": "CC72711A-B7BE-4AF2-8107-59AC844B43D3"},
    {
        "username": "BENJAMINMOORE23",
        "License API": "DF40E47F-582B-4065-B21D-B5793C29C3EE",
    },
    {
        "username": "BENJAMINMOORE",
        "License API": "F0E387B1-B283-403B-99FC-6410E64EC216",
    },
    {"username": "AVASMITH", "License API": "BE9C83D8-ED76-4D9D-8F79-A471FE25E07C"},
    {"username": "MICHAELJONES", "License API": "94924775-E07C-4A26-891D-085DC3F3EA1B"},
    {
        "username": "ISABELLATAYLOR",
        "License API": "3BB93D06-2696-427D-8775-54F79E94C0CA",
    },
    {"username": "OLIVIAJONES", "License API": "85DC7E91-212E-4E98-AB5C-9C9660D01766"},
    {"username": "AVATAYLOR", "License API": "F1A9C21F-5D84-4248-BD7B-DEB994D78559"},
    {"username": "OLIVIAMOORE", "License API": "62E0F39F-BEC9-461D-8E2A-A32B4CFF020B"},
    {"username": "SOPHIADAVIS", "License API": "0FA1242B-D2E6-4D7C-B36B-87B76BECB5A4"},
]


def extract_text_from_image(image_path, username, license_code):
    # OCR settings
    request_url = (
        "http://www.ocrwebservice.com/restservices/processDocument?gettext=true"
    )

    # Read image data
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Send request to OCRWebService.com
    response = requests.post(
        request_url, data=image_data, auth=(username, license_code)
    )
    print(response.status_code)
    if response.status_code == 401:
        # Unauthorized request
        print("Unauthorized request")
        return None
    elif response.status_code == 402:
        # Limit exceeded, try next account
        print("Limit exceeded for account:", username)
        return "limit_exceeded"
    # Decode output response
    jobj = json.loads(response.content)

    # Check for recognition error
    ocr_error = str(jobj.get("ErrorMessage", ""))
    if ocr_error:
        print("Recognition Error:", ocr_error)
        return None

    # Extracted text
    extracted_text = jobj.get("OCRText", [[""]])[0][0]
    return extracted_text


folder_names = ["1", "2"]
for folder_name in folder_names:
    images = os.listdir(folder_name)
    for image_path in images:
        for account in details:
            try:
                # Usage
                extracted_text = extract_text_from_image(
                    os.path.join(folder_name, image_path),
                    account["username"],
                    account["License API"],
                )
                if extracted_text is not None and extracted_text != "limit_exceeded":
                    with open(f"{folder_name}.txt", "a", encoding="utf-8") as f:
                        f.write(f"{extracted_text}\n")
                    break  # Break the loop if successful response is received
            except Exception as e:
                print(e)
