# Load data from Postgres to MinIO using Airflow

In this project, we will demonstrate how to export data from a PostgreSQL database to a temporary file in CSV format and then upload it to a MinIO bucket. The process will be orchestrated using Apache Airflow, and all components, including Airflow, PostgreSQL, and MinIO, will be hosted in Docker containers.

![alt text](https://github.com/annisayusoff/airflow/blob/efccd5e376c1a0da1620fc980dbd4d0b187f75cd/data%20flow.png?raw=true)
