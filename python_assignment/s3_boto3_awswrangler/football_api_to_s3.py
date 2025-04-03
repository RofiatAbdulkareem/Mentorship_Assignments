import pandas
import requests
import json
import boto3
import awswrangler as wr
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()
url = "http://api.football-data.org/v4/competitions/"
response = requests.get(url)
response.status_code

x = response.json()['competitions']
x

df = pandas.json_normalize(x)
df

session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

wr.s3.to_parquet (
    df= df, 
    path = "s3://rofiat-bucket/football_data.parquet", 
    dataset = False,
    #mode = 'append',
    boto3_session=session
    )