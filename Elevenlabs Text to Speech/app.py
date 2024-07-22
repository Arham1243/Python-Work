from flask import Flask, render_template, request, redirect, url_for, abort
from dotenv import load_dotenv
import os
import requests
from datetime import datetime

public_folder = "static"
app = Flask(__name__, static_url_path=f"/{public_folder}", static_folder=public_folder)

load_dotenv()
# api_key = os.getenv("XI_API_KEY")
app.secret_key = os.getenv("SECRET_KEY")
api_keys = [
    "e75325fa515016687c54717efd131baf",
    "26fd84de6bf6ef8856c3e8675fbb8d31",
    "4f1b34be92d658285f516874add0bde4",
    "520651c185cc1079fbc9d28a7d1cef0e",
    "0f43b0b2b8ce90f428027b182edbfc83",
    "6994e46d715b5dab8ecba50466225dea",
    "215b21443a9121a517d9b397dd05cdb1",
    "cfc0ab13cbb535a06066f708db30268b",
    "ae38df309bf93a9d0727bb13e45da8a4",
    "35ed200343e2dc1337897112d5ecd912",
    "ef35b492c9c33ca3e22e6f92b652609c",
    "dbc4df1c21bfda312a3f7c6a7ca3d212",
    "209af9781c6d16606da2d3a0368dec60",
    "dcbff155c3ca8865f6daf02967edc7a6",
    "90681b072d2711f2930c45a96799b569",
    "4369ff1cb95a48bffcd7b7df3fc73f02",
    "5db0807ca03f1ba02d7a6e7b075df5e7",
    "db68492a58a0dd885a3f9d9b0f562716",
    "b2313e01ea3dfef4a46c3859e8f8a9aa",
    "0905094ec3d61109d006acc79fd1b3bf",
    "1017ad4db0e45e06cc4a7e35fc4ef4e2",
    "42977fd356f9936502f2bab5103c4918",
    "e9fdd78a398ea6511678501808de6285",
    "43a243689d3e735f1cbc8514dc94b3b4",
    "5da4f8a73fb0eaf77515fdb412a1a63e",
    "79c5615d3cd25e61221b45ce2c1779ba",
    "50a81dd0d72a70370f373b825b78da4d",
    "2ec2216cb952763e8f70f8a2bb7bbe7a",
    "fc8c202fd2045ca54c2f68d8dc60cb9c",
    "ca3356ff49af9da04e68774c3a46c94b",
    "37dc4b396329129c4d0eece3b7890e55",
    "9b5f9cd54b8c22f19a7f4d3fb13df5ee",
    "3a215dd535f169217b1b53711f3bf7b8",
    "a3d92030771999acb2466acab5e3a190",
    "8807d6d33df1a2358f5cbd5a300acea6",
    "42124112fd7941d33c1acea6422c88ce",
    "cf81505047cbc04f85bd596f309e2784",
    "709bc6fb14a7b49d079616670ee3a656",
    "a2d194c55ff92598c6844eb302bbd36d",
    "5106321913cee3e0c667ce9153725c34",
    "d5d83625e76b3a89286589e21810431a",
    "de4b4192709e64adf2dde02bb42632cf",
    "edfab6766a6a2ae79447ca28e8368194",
    "32ec68aac4be22e683ead71e265b4b69",
    "b148b158a9b55148cde6bc008123ff7e",
    "e492f77a90a525b7439f5a1f0b1612b0",
    "e1a56cb464762736c4d5b948a2f0b347",
    "f7f3306979ac28a63cd13898fee6834b",
    "459c7686d26d2ae9ee075f8ef5c9e4d8",
    "42eec3a211d785555c63fdaad1163c73",
    "df2e5609b3f5ee6fbb50b0b118f38076",
    "ebb23cb56ba616542542cf3dead30d17",
    "9473238e03b02d12e7304792a53c407d",
    "22534ba0c0f1245d54398a40bf739e84",
    "7ef6db01a46cfe4ab89118621e93177e",
    "56712681cc34f0cff0d7ee68cf67521c",
    "aac20c81bb849b1a89ae70c219d40fc8",
    "166f36c256f33822ece10a088badc713",
    "c72f496ed9d4f11c8198d6dbb8263d47",
    "a859550a1a4ae444dd4bdc75493c920b",
]

api_key = api_keys[0]


def get_voices(url, api_key):
    try:
        headers = {
            "xi-api-key": api_key,
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        abort(500, description=f"Error fetching voices: {e}")


def convert_text_to_speech(text, voice_id, folder, api_key, file_name):
    try:
        CHUNK_SIZE = 1024
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        }

        data = {
            "text": text,
            "model_id": "eleven_turbo_v2",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
        }
        now = datetime.now()

        # filename = now.strftime("%d-%b-%Y-%H-%M-%S")

        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = f"{os.path.join(folder, file_name)}.mp3"
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        return file_path
    except requests.RequestException as e:
        abort(500, description=f"Error converting text to speech: {e}")


@app.route("/")
def home():
    audio_path = request.args.get("audio_path")

    try:
        voices = get_voices("https://api.elevenlabs.io/v1/voices", api_key)
    except abort:
        abort(500, description="Error fetching voices")

    data = {
        "all_voices": voices,
        "audio_path": audio_path if audio_path else None,
    }

    return render_template("index.html", data=data)


def split_text_into_chunks(text, chunk_size):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks

@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    text = request.form["text"]
    voice_id = request.form["voice_id"]
    file_name = request.form["filename"]

    try:
        converted_audio = convert_text_to_speech(
            text,
            voice_id,
            os.path.join(public_folder, "audio-files"),
            api_key,
            file_name,
        )
    except Exception as e:
        abort(500, description="Error converting text to speech: " + str(e))

    return redirect(url_for("home", audio_path=converted_audio))


# @app.route("/text-to-speech", methods=["POST"])
# def text_to_speech():

#     text = request.form["text"]
#     voice_id = request.form["voice_id"]
#     text_chunks = split_text_into_chunks(text, 2500)

#     # Initialize variables to keep track of API key usage
#     api_key_index = 0
#     converted_audios = []

#     for i, text_chunk in enumerate(text_chunks):
#         i += 13
#         try:
#             # Retrieve current API key
#             api_key = api_keys[api_key_index]

#             # Convert text chunk to speech
#             converted_audio = convert_text_to_speech(
#                 text_chunk,
#                 voice_id,
#                 os.path.join(public_folder, "audio-files"),
#                 api_key,
#                 i,
#             )

#             # Append the converted audio to the list
#             converted_audios.append(converted_audio)
#         except Exception as e:
#             abort(500, description="Error converting text to speech: " + str(e))

#         # Increment API key index, loop back to the beginning if necessary
#         api_key_index = (api_key_index + 1) % len(api_keys)

#     # Return the list of converted audio paths
#     return redirect(url_for("home", audio_paths=converted_audios))


@app.route("/voices")
def voices():
    try:
        voices = get_voices("https://api.elevenlabs.io/v1/voices", api_key)
    except abort:
        abort(500, description="Error fetching voices")

    data = {
        "all_voices": voices,
    }
    return render_template("voices.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
