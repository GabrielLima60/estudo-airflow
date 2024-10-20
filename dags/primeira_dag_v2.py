'''
primeira DAG v2: hello world
'''

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag(
    dag_id = "a_primeira_DAG_v1",
    start_date=datetime(2024, 10, 20),
    schedule="@daily",
    doc_md=__doc__,
)

def primeira_dag_v2():
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")
    start >> hello >> end

criar_DAG = primeira_dag_v2()