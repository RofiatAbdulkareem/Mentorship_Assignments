import pandas
import requests
import json
import boto3
import awswrangler as wr
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
response.status_code
x = response.json()['results']
x

df = pandas.json_normalize(x)
df
df_y = df[['gender','email', 'phone', 'cell']]
df_y
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)
wr.s3.to_parquet (
    df= df_y, 
    path = "s3://rofiat-bucket/random_user_data.parquet", 
    dataset = True,
    mode = 'append',
    boto3_session= session
    )