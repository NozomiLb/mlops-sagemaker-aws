import boto3
import os

def upload_to_s3(bucket_name, file_path, s3_file_key):
    s3 = boto3.client('s3')
    
    # Check if the file exists locally
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} does not exist.")
        return

    # Upload the file to S3
    try:
        s3.upload_file(file_path, bucket_name, s3_file_key)
        print(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_file_key}")
    except Exception as e:
        print(f"Failed to upload {file_path} to S3: {e}")

if __name__ == "__main__":
    bucket_name = 'sagemkr-detect-food'
    file_path = "calorie_data.csv"  # Example file path
    s3_file_key = "data/calorie_data.csv"

    upload_to_s3(bucket_name, file_path, s3_file_key)