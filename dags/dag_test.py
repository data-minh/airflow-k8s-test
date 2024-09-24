from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='dummy_test_dag',
    default_args=default_args,
    description='A simple test DAG using DummyOperator',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 9, 24),
    catchup=False,
) as dag:

    # Define tasks
    start_task = DummyOperator(
        task_id='start',
    )

    middle_task = DummyOperator(
        task_id='middle',
    )

    end_task = DummyOperator(
        task_id='end',
    )

    # Set task dependencies
    start_task >> middle_task >> end_task
