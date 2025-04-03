import pandas
import requests
import json
import boto3
import awswrangler as wr
import dotenv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define API URL to fetch 500 random user data
url = "https://randomuser.me/api/?results=500"

# Make an API request to fetch user data
response = requests.get(url)

# Checking response status
response.status_code

# Extract the 'results' key from the JSON response
x = response.json()['results']
x

# Normalize JSON data into a structured DataFrame
df = pandas.json_normalize(x)
df 

# Select specific columns (gender, email, phone, cell) for further processing
df_y = df[['gender', 'email', 'phone', 'cell']]
df_y

# Create a boto3 session using AWS credentials from environment variables
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

# Store the selected DataFrame in an S3 bucket in Parquet format
wr.s3.to_parquet(
    df=df_y, 
    path="s3://rofiat-bucket/random_user_data.parquet",
    dataset=True,
    mode='append',
    boto3_session=session
)
