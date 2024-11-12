from PIL import Image

# Function to resize an image while preserving its aspect ratio
def resize_image(input_image_path, output_image_path, max_width, max_height):
    # Open the original image
    image = Image.open(input_image_path)
    
    # Get the original image dimensions
    original_width, original_height = image.size
    
    # Calculate the aspect ratio
    aspect_ratio = original_width / original_height
    
    # Calculate new dimensions while preserving aspect ratio
    if original_width > original_height:
        new_width = min(max_width, original_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(max_height, original_height)
        new_width = int(new_height * aspect_ratio)
    
    # Resize the image with the new dimensions
    resized_image = image.resize((new_width, new_height))
    
    # Save the resized image
    resized_image.save(output_image_path)
    resized_image.show()
    print(f"Resized image saved to: {output_image_path}")

# Example usage
resize_image("C:/Users/Santhosh kumar/Pictures/images/San-Goku/IMG_20240109_083654.jpg", "D:/Random Programs/assets/output_resized_image.jpg", max_width=800, max_height=600) # Your inpout and output image's path comes in this line only
