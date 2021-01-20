#!/usr/bin/env bash
airflow db init
airflow db upgrade
airflow webserver