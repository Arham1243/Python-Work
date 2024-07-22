from PIL import Image
import os


def resize_image(input_path, output_path, desired_width, desired_height):
    # Open the image file
    original_image = Image.open(input_path)

    # Get the original width and height
    original_width, original_height = original_image.size

    # Calculate the proportional height to maintain the aspect ratio
    aspect_ratio = original_width / original_height
    calculated_height = int(desired_width / aspect_ratio)

    # Resize the image
    resized_image = original_image.resize((desired_width, calculated_height))

    # Save the resized image with the same name
    resized_image.save(output_path)


if __name__ == "__main__":
    # Set the path to your image file
    input_image_path = "images\\bg-banner.webp"

    # Set the desired width and height
    desired_width = 1200    
    desired_height = 400

    # Get the file name and ex  tension
    base_name, extension = os.path.splitext(os.path.basename(input_image_path))

    # Construct the output path with the same name and a new extension
    output_image_path = os.path.join(
        os.path.dirname(input_image_path), f"{base_name}_resized{extension}"
    )

    # Resize the image while maintaining the aspect ratio
    resize_image(input_image_path, output_image_path, desired_width, desired_height)

    print(f"Image resized and saved at: {output_image_path}")
