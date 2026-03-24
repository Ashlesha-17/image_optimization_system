# services/cloudinary_service.py
import cloudinary
import cloudinary.uploader
from config import CLOUD_NAME, API_KEY, API_SECRET  # ONLY this import, no circular stuff

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

def upload_image(file):
    """Uploads the given file to Cloudinary and returns the secure URL"""
    result = cloudinary.uploader.upload(file)
    return result['secure_url']