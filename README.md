# coinapi_streaming
A data engineering project with Kafka, Spark Streaming, dbt, Docker, Airflow, Terraform, GCP and much more!

# Streamify

A data pipeline with Kafka, Spark Streaming, dbt, Docker, Airflow, Terraform, GCP and much more!

## Description

### Objective

The project will stream cryptocurrencies data using the coincap api and create a data pipeline that consumess the real-time data. The data coming in would be real-time data on assets, rates, exchanges and markets. The data will be processed in real-time and stored to the data lake periodically. The hourly dbt job will then consume this data, transform it and create the desired tables for our dashboard to generate charts.


### Dataset

[CoinCap](https://docs.coincap.io/) is a useful tool for real-time pricing and market activity for over 1,000 cryptocurrencies. By collecting exchange data from thousands of markets, we are able to offer transparent and accurate data on asset price and availability.

Our API will offer insight into exactly which exchanges and markets contribute to our pricing.

For all endpoints, a single page offers 100 responses by default and supports up to 2,000 responses per page upon requests.



### Tools & Technologies

- Cloud - 
- Infrastructure as Code software - [**Terraform**](https://www.terraform.io)
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Stream Processing - [**Kafka**](https://kafka.apache.org), [**Spark Streaming**](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
- Orchestration - [**Airflow**](https://airflow.apache.org)
- Transformation - [**dbt**](https://www.getdbt.com)
- Data Lake - 
- Data Warehouse - 
- Data Visualization - 
- Language - [**Python**](https://www.python.org)

### Architecture



### Final Result


## Setup





- Terraform
  - [Setup Terraform](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/windows.md#terraform)


### Get Going!




### Debug

If you run into issues, see if you find something in this debug [guide](setup/debug.md).
### How can I make this better?!


### Special Mentions
I'd like to thank the [DataTalks.Club](https://datatalks.club) for offering this Data Engineering course for completely free. All the things I learnt there, enabled me to come up with this project. If you want to upskill on Data Engineering technologies, please check out the [course](https://github.com/DataTalksClub/data-engineering-zoomcamp). :)
