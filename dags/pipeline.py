import csv
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook  
from tempfile import NamedTemporaryFile


default_args = {
    'owner': 'annisa',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}


def postgres_to_s3(ds_nodash, next_ds_nodash):

    #step1: query data from postgres db
    hook = PostgresHook(postgres_conn_id="postgres_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(f"select * from orders where date >= '{ds_nodash}' and date <= '{next_ds_nodash}'")

    #step2: upload text file into S3 using tempfile
    with NamedTemporaryFile(mode="w", suffix=ds_nodash) as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
        cursor.close()
        conn.close()
        logging.info(f"Saved orders data in text file : dags/get_orders_{ds_nodash}.txt")

        #step2: upload text file into S3
        s3_hook = S3Hook(aws_conn_id="minio_conn")
        s3_hook.load_file(
            filename=f.name,
            key=f"orders/{ds_nodash}.txt",
            bucket_name="airflow",
            replace=True
        )
        logging.info(f"Orders file {f.name} has been pushed to S3!")


with DAG (dag_id='etl_v02', default_args=default_args, start_date=datetime(2024,5,10), schedule='@yearly') as dag:
    task1 = PythonOperator(
        task_id="postgres_to_s3",
        python_callable=postgres_to_s3
    )

    task1


