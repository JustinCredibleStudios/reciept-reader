# Script to Create S3 Bucket
# Author: Justin Miller
# Date: 9/30/2024

# Importing Libraries
import logging
import boto3
from botocore.exceptions import ClientError

#Defining Variables
bucket_name = 'recieptreader'
region = 'us-east-1'

# Defining functions 
def create_bucket(bucket_name, region):
    """
    Create an S3 bucket in the specified region.

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created successfully, else False
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True