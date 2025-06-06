import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
url = os.getenv('API_KEY')

# Make a GET request to the API
response = requests.get(url)


def guardian(url):
    """
    Fetches data from the URL, extracts relevant fields,
    normalizes the data into a DataFrame, and returns the DataFrame.

    Parameters:
        url (str): The API endpoint.

    Returns:
        df: A DataFrame containing the response data.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        guardian_response = data['response']['results']
        df = pd.json_normalize(guardian_response)
        return df
    else:
        print("Error: Unable to fetch data from the API")


df = guardian(url)

session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

wr.s3.to_parquet(
    df=df,
    path='s3://rofiat-bucket/football_data',
    dataset=True,
    mode='append',
    boto3_session=session
)
