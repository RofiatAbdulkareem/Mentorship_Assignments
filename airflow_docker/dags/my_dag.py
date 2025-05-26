from airflow import DAG
from airflow.operators.python import PythonOperator
from random_user_to_S3 import random_user_to_s3

default_args = {
    'owner': 'rofiat',
    'retries': 1
}

dag = DAG(
    dag_id = "dag1",
    description = "This is my dag for random users generation",
    default_args = default_args
)

extract_to_s3 = PythonOperator(
    task_id = "extract_to_s3",
    dag = dag,
    python_callable = random_user_to_s3
)

extract_to_s3
