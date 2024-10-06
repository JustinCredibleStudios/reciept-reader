# File uploader
# Justin S. Miller
# 10/6/2024

# Importing Libraries
import os
import boto3

# Defining the source folder
source_folder = "C:\\Users\\Jusrin S. Millero\\OneDrive\\Desktop\\CodeProjects\\Receipt_Reader\\files"

# Listing the files in the source folder
files = os.listdir(source_folder)

# Checking if the folder is empty
if not files:
    print("Folder is empty")
else:
    print("Folder is not empty")
    
# Connecting to S3 bucket
s3 = boto3.client('s3')
bucket_name = 'recieptreader'

# Uploading files to S3 bucket
for file in files:
    file_path = os.path.join(source_folder, file)
    s3.upload_file(file_path, bucket_name, file)