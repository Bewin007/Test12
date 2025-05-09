import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                resized_img = img.resize(size)
                resized_img.save(output_path)
                print(f"Resized and saved: {output_path}")

# Example usage
resize_images("input", "output")
