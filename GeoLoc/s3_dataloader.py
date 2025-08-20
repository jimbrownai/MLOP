import boto3
import os

CACHE_DIR = './.s3cache'
os.makedirs(CACHE_DIR, exist_ok=True)

os.environ['AWS_ACCESS_KEY_ID'] = ''
os.environ['AWS_SECRET_ACCESS_KEY'] = ''
os.environ['AWS_DEFAULT_REGION'] = ''

s3 = boto3.client('s3')
bucket = 'mlopsp3'
prefix = '50_most_famous_places/'
local_dir = 'train/'

def download_s3_folder(bucket, prefix, local_dir):
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if key.endswith("/"):  
                continue
            local_path = os.path.join(local_dir, os.path.relpath(key, prefix))
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            if not os.path.exists(local_path):  
                s3.download_file(bucket, key, local_path)
                print(f"Downloaded {key} → {local_path}")

# download_s3_folder(bucket, prefix, local_dir)

import boto3
import os

def upload_test_image(file_path, bucket_name, folder="test_images"):

    # Extract filename
    file_name = os.path.basename(file_path)
    
    s3_key = f"{folder}/{file_name}"
    
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name, s3_key)
    
    s3_uri = f"s3://{bucket_name}/{s3_key}"
    print(f"Uploaded {file_name} → {s3_uri}")
    
    return s3_uri

def upload_test_images(file_paths, bucket_name, folder="test_images"):
    uris = []
    for f in file_paths:
        uris.append(upload_test_image(f, bucket_name, folder))
    return uris



# filepath = "resources/50_most_famous_places/Atomium/0a52b43208.jpg"
# upload_test_image(filepath,bucket)