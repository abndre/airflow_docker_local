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
export AIRFLOW_HOME=/Users/andre/airflow_dev

echo $AIRFLOW_HOME

pip install apache-airflow

source /Users/andre/venv38/bin/activate

airflow db init
```