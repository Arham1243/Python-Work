from PIL import Image
import os

def convert_webp_to_png(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all files in the input folder
    files = os.listdir(input_folder)
    
    # Iterate over each file
    for file_name in files:
        # Check if the file is a WebP image
        if file_name.lower().endswith('.webp'):
            # Open the WebP image
            webp_image = Image.open(os.path.join(input_folder, file_name))
            
            # Convert the WebP image to PNG
            png_image = webp_image.convert("RGBA")
            
            # Create the output file name by replacing .webp with .png
            output_file_name = os.path.splitext(file_name)[0] + '.png'
            
            # Save the PNG image to the output folder
            png_image.save(os.path.join(output_folder, output_file_name), format='PNG')
            print(f"Converted {file_name} to PNG.")
    
    print("Conversion complete.")

# Provide input and output folders
input_folder = 'images'  # Replace 'input_folder_path' with the path to your input folder containing WebP images
output_folder = 'images'  # Replace 'output_folder_path' with the path to your output folder where PNG images will be saved

# Convert WebP images to PNG
convert_webp_to_png(input_folder, output_folder)
