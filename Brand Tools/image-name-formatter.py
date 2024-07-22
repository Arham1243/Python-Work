import os

folder_name = "images"
files = os.listdir(folder_name)
for i, file in enumerate(files):
    i += 1
    ext = file.split(".")[-1]
    if i < 10:
        # Format the index with leading zero
        new_name = f"0{ic:\Users\11007\Desktop\port-11.webp}.{ext}"
    else:
        # Format the index without leading zero
        new_name = f"{ic:\Users\11007\Desktop\port-11.webp}.{ext}"
    os.rename(f"{folder_name}/{file}", f"{folder_name}/{new_name}")
