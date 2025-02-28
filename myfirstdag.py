from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define the default arguments for our DAG
default_args = {
    'owner': 'me',
    'start_date': datetime(2024, 2, 7),
    'retries': 1,  # If task fails, try 1 more time
    'retry_delay': timedelta(minutes=5)  # Wait 5 minutes before retry
}

# Create the DAG
dag = DAG(
    'my_first_dag',  # Name of your DAG
    default_args=default_args,
    schedule_interval='@daily'  # Run once every day
)

# Define some example functions
def get_data():
    print("Downloading data...")
    # Here you would add code to download data

def process_data():
    print("Processing data...")
    # Here you would add code to process data

def send_email():
    print("Sending email report...")
    # Here you would add code to send email

# Create the tasks
task1 = PythonOperator(
    task_id='get_data',
    python_callable=get_data,
    dag=dag
)

task2 = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag
)

task3 = PythonOperator(
    task_id='send_email',
    python_callable=send_email,
    dag=dag
)

# Set the order of tasks
task1 >> task2 >> task3 