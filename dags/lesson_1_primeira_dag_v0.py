"""
Primeira DAG v0: hello world
"""

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="primeira_dag_v0",
    start_date=datetime(2024, 10, 19),
    schedule="@daily",
    doc_md=__doc__,
):
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")

(start >> hello >> end)