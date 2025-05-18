from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='feature_ingestion_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    feast_apply = BashOperator(
        task_id='feast_apply',
        bash_command='python /app/scripts/feast_apply_validate.py'
    )

    train_model = BashOperator(
        task_id='train_model',
        bash_command='python /app/src/train.py'
    )

    feast_apply >> train_model