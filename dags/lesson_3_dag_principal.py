# DAG Principal

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import pendulum
import pprint

def print_principal(**kwargs):
    print("DAG principal")
    pprint.pprint(kwargs)
    return "principal"

with DAG(
    dag_id = "DAG_principal",
    schedule = "* * * * *",
    start_date=pendulum.datetime(2024, 10, 21, tz="America/Sao_Paulo"),
    catchup=True,
) as dag:
    start = EmptyOperator(task_id="start")
    python_principal = PythonOperator(
        task_id="python_principal", python_callable=print_principal
    )
    end= EmptyOperator(task_id="end")

start >> python_principal >> end