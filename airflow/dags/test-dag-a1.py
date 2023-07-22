from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "depends_on_past": False,
    "start_date": datetime(2023, 7, 22),
    "retries": 0
}

with DAG(
    dag_id="test-dag-a1",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=["sync-sub-a"],
) as dag:

    test_task = BashOperator(
        task_id="test_task",
        bash_command="echo 'Hello K8S Airflow World from DAG A1'",
        do_xcom_push=False,
    )
    