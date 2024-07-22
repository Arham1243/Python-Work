from PIL import Image
import os

primary_folder = "folder-images"
folders = os.listdir(primary_folder)


def convert_to_webp(file, folder_name, images):
    ext = file.split(".")[-1]
    if ext.lower() not in ["jpg", "jpeg", "png"] or f"{file}.webp" in images:
        return

    try:
        input_image = Image.open(os.path.join(folder_name, file))
        output_file = os.path.join(folder_name, f"{file.split('.')[0]}.webp")
        quality = 80
        input_image.save(output_file, "webp", quality=quality)
        print(f"Image saved as {output_file} with quality {quality}")
    except Exception as e:
        print(f"Could not identify image file: {e}")


def delete_old_images(images, folder_name):
    for file in images:
        ext = file.split(".")[-1]
        if ext.lower() in ["jpg", "jpeg", "png"]:
            os.remove(os.path.join(folder_name, file))


def rename_images(images, folder_name):
    webp_images = [file for file in images if file.endswith(".webp")]
    for i, file in enumerate(webp_images, start=1):
        old_path = os.path.join(folder_name, file)
        new_name = os.path.join(folder_name, f"{i}.webp")
        os.rename(old_path, new_name)


def compressor():
    for folder in folders:
        images = os.listdir(os.path.join(primary_folder, folder))
        for image in images:
            convert_to_webp(image, os.path.join(primary_folder, folder), images)
        rename_images(images, os.path.join(primary_folder, folder))
        delete_old_images(images, os.path.join(primary_folder, folder))


if __name__ == "__main__":
    compressor()
