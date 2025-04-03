#importing the necessary libraries
import pandas
import requests
import json
import boto3
import awswrangler as wr
import dotenv
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the API endpoint URL for retrieving football competition data
url = "http://api.football-data.org/v4/competitions/"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check the status code of the response to ensure successful retrieval
response.status_code

# Extract the list of competitions from the JSON response
x = response.json()['competitions']

# Normalize the JSON data into a pandas DataFrame
# This flattens nested structures, making it easier to analyze
df = pandas.json_normalize(x)

df 

# Create a boto3 session using credentials stored in environment variables
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

# Save the DataFrame as a Parquet file in an S3 bucket using awswrangler
wr.s3.to_parquet(
    df=df,  
    path="s3://rofiat-bucket/football_data.parquet", 
    dataset=False,  
    # mode='append',
    boto3_session=session
)