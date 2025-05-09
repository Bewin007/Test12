from PIL import Image

def resize_image(input_path, output_path, size=(300, 200)):
    with Image.open(input_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path)
        print(f"Image saved to {output_path} with size {size}")

# Example usage:
if __name__ == "__main__":
    input_image = "input.jpg"        # Replace with your image file
    output_image = "output.jpg"      # Output file path
    resize_image(input_image, output_image)
