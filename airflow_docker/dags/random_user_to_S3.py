import awswrangler as wr
import boto3
import pandas
import requests
from airflow.models import Variable

url = "https://randomuser.me/api/?results=10"
response = requests.get(url)

def random_user_to_s3():
    """ 
    This function fetches 10 random user data from an API,
    and returns a dataframe
    """
    if response.status_code == 200:
        x = response.json()['results']
        df = pandas.json_normalize(x)
        df_y = df[['gender', 'email', 'phone', 'cell']]
        
        session = boto3.Session(
            aws_access_key_id=Variable.get('ACCESS_KEY'),
            aws_secret_access_key=Variable.get('SECRET_KEY'),
            region_name='eu-central-1'
        )
        wr.s3.to_parquet(
            df=df_y,
            path="s3://rofiat-bucket/ten_random_user_data_using_airflow",
            dataset=True,
            mode='append',
            boto3_session=session
        )
        print("Data written to s3 successfully")
        return df_y
    else:
        print("Error: Unable to fetch data from the API")
