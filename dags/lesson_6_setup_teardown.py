# The idea here is to be able to skip to thee last task in case there is an error in the middle.
# That guarantees that the dag won't keep running and consuming resources 

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pendulum
import numpy as np

def random_error():
    num = np.random.randint(0,1)
    if num == 0:
        return 0
    else:
        raise ValueError('Error found. Deleting C:\\Windows\\System32...')
    
with DAG(
    "dag_setup_teardown",
    schedule_interval = timedelta(days=1),
    start_date=pendulum.datetime(2024, 10, 30, tz='UTC'),
    catchup=True

) as dag:
    start = EmptyOperator(task_id='start')
    tarefa_inicio = BashOperator(task_id = 'tarefa_inicio', bash_command= "echo 'first task'").as_setup()
    tarefa_normal = PythonOperator(task_id = "random_error", python_callable=random_error)
    tarefa_fim = BashOperator(task_id='tarefa_fim', bash_command= "echo 'last task'").as_teardown(setups=tarefa_inicio)
    end = EmptyOperator(task_id='end')

start >> tarefa_inicio >> tarefa_normal >> tarefa_fim >> end