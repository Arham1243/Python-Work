import os

imgExts = [".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"]
docExts = [".docx", ".xlsx", ".pdf", ".pub", ".pptx", ".accdb"]
videoExts = [".mp4", ".mp3", ".webm", ".mov", ".flv"]
zipExts = [".zip", ".rar", ".rar5"]
adobeExts = [".psd", ".ai"]
others = []


files = os.listdir()
files.remove('index.py')


def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


createFolder('Images')
createFolder('Docs')
createFolder('Videos')
createFolder('Others')
createFolder('Zips')
createFolder('Adobes')


images = [file for file in files if os.path.splitext(file)[
    1].lower() in imgExts]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
videos = [file for file in files if os.path.splitext(file)[
    1].lower() in videoExts]
zip = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]
adobes = [file for file in files if os.path.splitext(file)[
    1].lower() in adobeExts]


for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in videoExts) and os.path.isfile(file):
        others.append(file)


move("Images", images)
move("Videos", videos)
move("Docs", docs)
move("Zips", zip)
move("Adobes", adobes)
move("Others", others)
