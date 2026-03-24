# services/s3_service.py

import boto3
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def upload_to_s3(file_path, file_name):
    s3.upload_file(file_path, BUCKET_NAME, file_name)
    
    url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"
    return url