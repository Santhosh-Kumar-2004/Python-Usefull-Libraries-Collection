from PIL import Image, ImageDraw, ImageFont

# Function to add a watermark to an image
def add_watermark(input_image_path, output_image_path, watermark_text, position='center', opacity=128):
    # Open the input image
    image = Image.open(input_image_path).convert("RGBA")
    
    # Make a blank image for the watermark text
    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    
    # Choose a font and size
    font_size = int(min(image.size) / 10)  # Adjust font size relative to image dimensions
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # Use default font if "arial.ttf" is not found
    
    # Initialize drawing context
    draw = ImageDraw.Draw(txt_layer)
    
    # Get the text bounding box and calculate position
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)  # Get bounding box of text
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    if position == 'center':
        position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
    
    # Add text to the transparent layer with specified opacity
    draw.text(position, watermark_text, font=font, fill=(255, 255, 255, opacity)) # type: ignore
    
    # Combine the watermark layer with the original image
    watermarked_image = Image.alpha_composite(image, txt_layer)
    
    # Save the output in RGB format (removing alpha for compatibility)
    watermarked_image = watermarked_image.convert("RGB")
    watermarked_image.save(output_image_path)
    watermarked_image.show()
    print("Watermark added and saved to:", output_image_path)

# Example usage
# add_watermark("path/to/input_image.jpg", "path/to/output_image_with_watermark.jpg", "Sample Watermark", position='center')

add_watermark("C:/Users/Santhosh kumar/Pictures/images/San-Goku/IMG_20240109_083654.jpg", "D:/Random Programs/assets/Sample_Watermark.jpg", "Santhosh's Image", position='center')
