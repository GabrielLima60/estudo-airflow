from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task
import pendulum
import pprint

with DAG(
    dag_id="python_operator_v2",
    schedule="* * * * *",
    start_date= pendulum.datetime(2024, 10, 20, 12, 30, tz="America/Sao_Paulo"),
    catchup=True,
) as dag:
    start = EmptyOperator(task_id= "start")
    end = EmptyOperator(task_id="end")

    @task(task_id="python")
    def meu_codigo(ds=None, **kwargs):
        pprint.pprint(kwargs)
        print(ds)
        return "retorno"
        
    python = meu_codigo()

start >> python >> end