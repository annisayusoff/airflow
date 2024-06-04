# Load data from Postgres to MinIO using Airflow

In this project, we will demonstrate how to export data from a PostgreSQL database to a temporary file in CSV format and then upload it to a MinIO bucket. The process will be orchestrated using Apache Airflow, and all components, including Airflow, PostgreSQL, and MinIO, will be hosted in Docker containers.

![alt text](https://github.com/annisayusoff/airflow/blob/efccd5e376c1a0da1620fc980dbd4d0b187f75cd/data%20flow.png?raw=true)

- You can check the code for this process in below link:
https://github.com/annisayusoff/airflow/blob/5f1b6959e96236dd199d6a92fac7b8a6b78a7441/dags/pipeline.py

- You can get the airflow docker-compose from below link:
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

(fetching the docker-compose by running **curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'**)
