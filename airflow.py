from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from bigquery_table import copy_bigquery

# Name of DAG Workflow
WORFKLOW_DAG_ID = 'copy_bigquery'
# Cron scheduler
WORKFLOW_SCHEDULE_INTERVAL = "0 7 * * *"
DEFAULT_ARGS = {
        'owner': 'airflow',
        'depends_on_past': False,
        'email': ['airflow@airflow.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'retry_delay': timedelta(minutes=5)
}


dag = DAG(dag_id = WORFKLOW_DAG_ID,
          schedule_interval = WORKFLOW_SCHEDULE_INTERVAL,
          default_args = DEFAULT_ARGS,
          start_date = datetime(2023, 1, 16)
         )
        
task_1 = DummyOperator(task_id='start')

task_2 = PythonOperator(task_id = 'copy_bigquery',
                        python_callable = copy_bigquery,
                        dag = dag,
                       )

task_3 = DummyOperator(task_id = 'end')

task_1 >> task_2 >> task_3

