import os

import awswrangler as wr
import boto3
import pandas as pd
import response
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


url = "https://jobicy.com/api/v2/remote-jobs?" \
        "count=20&geo=usa&industry=marketing&tag=seo"

response = response.response

df = pd.json_normalize(response['jobs'])

session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    region_name='eu-central-1'
)

wr.s3.to_parquet(
    df=df,
    path="s3://rofiat-bucket/job_response.parquet",
    dataset=False,
    # mode='append',
    boto3_session=session
)
