# Airflow Docker Local

#project structure
```
root/
├── dags/
│   └── dummy_dag.py
├── scripts/
│   └── entrypoint.sh
├── logs/
├── .env
└── docker-compose.yml
```

# Commands

```
# coloque seu $PWD do airflow
export AIRFLOW_HOME=/Users/andre/airflow_dev

echo $AIRFLOW_HOME

pip install apache-airflow

source /Users/andre/venv38/bin/activate

airflow db init
```

Algum erro de permissao use:
```
chmod -R 777 scripts
```



Deletando processos airflow em Daemon

```
ps aux | grep 'airflow scheduler'

kill $(ps -ef | grep "airflow scheduler" | awk '{print $2}')
```

Variavel local para o projeto
```
export AIRFLOW_HOME=/Users/andresantosbarrosdasilva/Documents/airflow_dev
````

# Erros Comuns

Se ocorrer este erro
```
[2021-01-19 10:49:27,436] {local_task_job.py:118} INFO - Task exited with return code Negsignal.SIGABRT
```

utilize isto:

```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```