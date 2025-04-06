import os

import awswrangler as wr
import boto3
import pandas
import requests
from dotenv import load_dotenv

load_dotenv()

url = "http://api.football-data.org/v4/competitions/"


response = requests.get(url)

if response.status_code == 200:
    football_response = response.json()['competitions']
    df = pandas.json_normalize(football_response)

session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

wr.s3.to_parquet(
    df=df,
    path="s3://rofiat-bucket/football_data.parquet",
    dataset=False,
    # mode='append',
    boto3_session=session
)
