from PIL import Image, ImageEnhance, ImageFilter

# Function to apply various filters to an image
def apply_filter(input_image_path, output_image_path, filter_type="grayscale"):
    # Open the original image
    image = Image.open(input_image_path)
    
    if filter_type == "grayscale":
        # Convert the image to grayscale
        filtered_image = image.convert("L")
    elif filter_type == "sepia":
        # Apply sepia filter
        sepia_image = image.convert("RGB")
        pixels = sepia_image.load()
        
        for i in range(sepia_image.width):
            for j in range(sepia_image.height):
                r, g, b = sepia_image.getpixel((i, j)) # type: ignore
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                if tr > 255:
                    tr = 255
                if tg > 255:
                    tg = 255
                if tb > 255:
                    tb = 255
                pixels[i, j] = (tr, tg, tb) # type: ignore
        filtered_image = sepia_image
    elif filter_type == "blur":
        # Apply blur filter
        filtered_image = image.filter(ImageFilter.GaussianBlur(radius=5))
    elif filter_type == "sharpen":
        # Apply sharpen filter
        enhancer = ImageEnhance.Sharpness(image)
        filtered_image = enhancer.enhance(2.0)  # 2.0 is the sharpness factor
    else:
        print(f"Filter '{filter_type}' not recognized. Please choose 'grayscale', 'sepia', 'blur', or 'sharpen'.")
        return
    
    # Save the filtered image
    filtered_image.save(output_image_path)
    filtered_image.show()
    print(f"Filtered image saved to: {output_image_path}")

# Example usage
apply_filter("c:/Users/Santhosh kumar/Pictures/images/San-Goku/santhosh.jpf.jpg", "D:/Random Programs/assets/output_grayscale_image.jpg", filter_type="grayscale")
apply_filter("c:/Users/Santhosh kumar/Pictures/images/San-Goku/santhosh.jpf.jpg", "D:/Random Programs/assets/output_sepia_image.jpg", filter_type="sepia")
apply_filter("c:/Users/Santhosh kumar/Pictures/images/San-Goku/santhosh.jpf.jpg", "D:/Random Programs/assets/output_blurred_image.jpg", filter_type="blur")
apply_filter("c:/Users/Santhosh kumar/Pictures/images/San-Goku/santhosh.jpf.jpg", "D:/Random Programs/assets/output_sharpened_image.jpg", filter_type="sharpen")
