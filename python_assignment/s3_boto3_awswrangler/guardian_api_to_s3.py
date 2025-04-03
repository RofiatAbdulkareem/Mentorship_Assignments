import requests
import json
import pandas as pd
import boto3
import awswrangler as wr
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
url = os.getenv('API_KEY')
response = requests.get(url)
data = response.json()
data
api_result = data['response']['results']
api_result

df =pd.json_normalize(api_result)
df
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)
wr.s3.to_parquet(
    df = df,
    path='s3://rofiat-bucket/football_data',
    dataset=True,
    mode = 'append',
    boto3_session= session
)

def guardian(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        duh = data['response']['results']
        df = pd.json_normalize(duh)
        return df
    else:
        print("error")
guardian(url)
