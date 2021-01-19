from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
# from airflow.operators.docker_operator import DockerOperator
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
        'owner'                 : 'airflow',
        'description'           : 'Use of the DockerOperator',
        'depend_on_past'        : False,
        'start_date'            : datetime(2018, 1, 3),
}

dag = DAG('docker_dag', default_args=default_args, schedule_interval="*/5 * * * *", catchup=False)

t1 = BashOperator(
        task_id='print_current_date',
        bash_command='date',
        dag=dag
)

t2 = DockerOperator(
        task_id='docker_command',
        image='ubuntu',
        api_version='auto',
        auto_remove=True,
        command="echo Hello DOCKER",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",      
        dag=dag
)

t3 = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world"',
        dag=dag
)

t1 >> t2 >> t3