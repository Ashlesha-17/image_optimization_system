# services/image_service.py

from PIL import Image

def process_image(input_path, output_path, width=800, quality=60):
    img = Image.open(input_path)
    
    # Resize
    img = img.resize((width, width))
    
    # Compress
    img.save(output_path, optimize=True, quality=quality)
    
    return output_path