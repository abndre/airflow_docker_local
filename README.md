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