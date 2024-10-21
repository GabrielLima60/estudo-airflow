# DAG LatestOnlyOperator

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.latest_only import LatestOnlyOperator
import pendulum

def f_print():
    print("DAG LatestOnlyOperator")
    return "latest"

with DAG(
    dag_id = "DAG_LatestOnlyOperator",
    schedule="0 15 * * *",
    start_date=pendulum.datetime(2024, 10, 21, tz="America/Sao_Paulo"),
    catchup=True,
) as dag:
    start = EmptyOperator(task_id="start")
    latest= LatestOnlyOperator(task_id="latest")
    python_principal = PythonOperator(
        task_id="python_principal", python_callable= f_print
    )
    end = EmptyOperator(task_id="end")

start >> latest >> python_principal >> end