#!/usr/bin/env bash
export AIRFLOW_HOME=/opt/airflow
airflow db init
airflow db upgrade


airflow users create --role Admin --username admin \
--firstname peter \
--lastname parker \
--email peter.parker@spyder.com \
--password admin

airflow webserver