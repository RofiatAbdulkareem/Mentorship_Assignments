import os

import awswrangler as wr
import boto3
import pandas
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://randomuser.me/api/?results=500"
response = requests.get(url)

if response.status_code == 200:
    x = response.json()['results']
    df = pandas.json_normalize(x)
    df_y = df[['gender', 'email', 'phone', 'cell']]
else:
    print("Error: Unable to fetch data from the API")

session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

wr.s3.to_parquet(
    df=df_y,
    path="s3://rofiat-bucket/random_user_data.parquet",
    dataset=True,
    mode='append',
    boto3_session=session
)
