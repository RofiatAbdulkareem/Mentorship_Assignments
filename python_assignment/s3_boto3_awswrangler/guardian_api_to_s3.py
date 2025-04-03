import requests
import json
import pandas as pd
import boto3
import awswrangler as wr
import os
import dotenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
url = os.getenv('API_KEY')

# Make a GET request to the API
response = requests.get(url)

def guardian(url):
    """
    Fetches data from the given URL, extracts relevant JSON fields, 
    normalizes the data into a Pandas DataFrame, and returns the DataFrame.

    Parameters:
        url (str): The API endpoint URL.

    Returns:
        pd.DataFrame: A DataFrame containing the normalized API response data.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        duh = data['response']['results']
        df = pd.json_normalize(duh)
        return df
    else:
        print("Error: Unable to fetch data from the API")

df = guardian(url)

# Create a boto3 session using AWS credentials from environment variables
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

# Save DataFrame as a Parquet file in an S3 bucket
wr.s3.to_parquet(
    df=df,
    path='s3://rofiat-bucket/football_data',
    dataset=True,
    mode='append',
    boto3_session=session
)