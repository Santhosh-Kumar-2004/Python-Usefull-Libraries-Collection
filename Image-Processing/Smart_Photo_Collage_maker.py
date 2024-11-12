from PIL import Image
import os
import math

# Function to load and resize images to a target size
def load_and_resize_images(image_paths, target_size):
    images = []
    for path in image_paths:
        img = Image.open(path)
        img = img.resize(target_size, Image.LANCZOS)  # type: ignore # Updated to LANCZOS
        images.append(img)
    return images

# Function to calculate the grid size based on the number of images
def calculate_grid_size(num_images):
    grid_size = math.ceil(math.sqrt(num_images))  # Square root to get closest square layout
    return grid_size, grid_size

# Function to create a collage by arranging images on a blank canvas
def create_collage(images, grid_size, target_size):
    collage_width = grid_size[0] * target_size[0]
    collage_height = grid_size[1] * target_size[1]
    
    # Create a blank canvas for the collage
    collage_image = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))
    
    # Place each image on the canvas
    for i, img in enumerate(images):
        x = (i % grid_size[0]) * target_size[0]
        y = (i // grid_size[0]) * target_size[1]
        collage_image.paste(img, (x, y))
    
    return collage_image

# Main function to generate the collage
def generate_collage(image_folder, output_path, target_size=(200, 200)):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get paths for all images in the folder
    image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('jpg', 'png'))]
    
    # Load and resize images
    images = load_and_resize_images(image_paths, target_size)
    
    # Calculate the grid layout
    grid_size = calculate_grid_size(len(images))
    
    # Create the collage
    collage_image = create_collage(images, grid_size, target_size)
    
    # Save and display the collage
    collage_image.save(output_path)
    collage_image.show()

# Example usage
# generate_collage("D:/Random Programs/assests/images", "D:/Random Programs/assests/output_collage.jpg")

generate_collage("C:/Users/Santhosh kumar/Pictures/For gudiya", "D:/Random Programs/assets/output_collage.jpg")
