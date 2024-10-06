# Script to Create S3 Bucket
# Author: Justin Miller
# Date: 9/30/2024

# Importing Libraries
import logging
import boto3
import os

#AWS Credentials
r2session = boto3.Session(region_name='us-east-1')
s3client = r2session.client('s3')
#Defining Variables
bucket_name = 'recieptreader'
s3client.create_bucket(Bucket=bucket_name)