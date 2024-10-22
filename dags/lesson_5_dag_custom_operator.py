from airflow import DAG
from airflow.operators.empty import EmptyOperator
from custom_operators.lesson_5_hello_operator import HelloOperator
import pendulum

with DAG(
    dag_id="DAG_CustomOperator",
    schedule= "* * * * *",
    start_date=pendulum.datetime(2024, 10, 22, tz="America/Sao_Paulo"),
    catchup=False
) as dag:
    start = EmptyOperator(task_id="start")
    meu_operador = HelloOperator(task_id="hello", name = "Gabriel Lima")
    end = EmptyOperator(task_id="end")

start >> meu_operador >> end