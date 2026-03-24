from flask import Flask, render_template, request, send_file
from services.cloudinary_service import upload_image
import requests
from io import BytesIO

app = Flask(__name__)

# Function to get image size by downloading the image
def get_size(url):
    response = requests.get(url)
    size = len(response.content)
    return size / 1024  # KB

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    platform = request.form.get('platform')
    img_format = request.form.get('format', 'jpeg').lower()

    # Convert 'jpeg' to 'jpg' for Cloudinary
    if img_format == 'jpeg':
        img_format = 'jpg'

    # Upload original image
    original_url = upload_image(file)

    # Set default dimensions
    width, height = 500, 500
    suggestion = f"Balanced optimization ({img_format.upper()})"

    # Platform-based optimization
    if platform == "instagram":
        width, height = 600, 600
        suggestion = f"Optimized for Instagram ({img_format.upper()})"
    elif platform == "whatsapp":
        width, height = 400, 700
        suggestion = f"Optimized for WhatsApp ({img_format.upper()})"

    # Correct Cloudinary URL transformation with format conversion
    parts = original_url.split("/upload/")
    optimized_url = f"{parts[0]}/upload/w_{width},h_{height},c_fill,q_40,f_{img_format}/{parts[1]}"

    # Get sizes
    original_size = get_size(original_url)
    optimized_size = get_size(optimized_url)
    reduction = ((original_size - optimized_size) / original_size) * 100

    return render_template(
        'index.html',
        original=original_url,
        optimized=optimized_url,
        suggestion=suggestion,
        original_size=round(original_size, 2),
        optimized_size=round(optimized_size, 2),
        reduction=round(reduction, 2)
    )

@app.route('/download')
def download():
    optimized_url = request.args.get('url')
    response = requests.get(optimized_url)
    img_bytes = BytesIO(response.content)

    # Determine mimetype based on extension
    ext = optimized_url.split('.')[-1].lower()
    mimetype = "image/jpeg"
    if ext == "png":
        mimetype = "image/png"
    elif ext == "webp":
        mimetype = "image/webp"

    return send_file(
        img_bytes,
        as_attachment=True,
        download_name=f"optimized_image.{ext}",
        mimetype=mimetype
    )

if __name__ == '__main__':
    app.run(debug=True)