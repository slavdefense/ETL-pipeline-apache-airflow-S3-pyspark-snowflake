from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import youtube_api as youtube
# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
)

# Dummy start task
start = EmptyOperator(task_id='start', dag=dag)

# Python task example
def example_task(**kwargs):
    print("This is an example task.")
    # Insert your actual task code here
    youtube.extract_youtube_data()    
    

example_python_task = PythonOperator(
    task_id='example_python_task',
    python_callable=example_task,
    dag=dag,
)

# Dummy end task
end = EmptyOperator(task_id='end', dag=dag)

# Define task dependencies
start >> example_python_task >> end
