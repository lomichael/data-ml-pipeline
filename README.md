# Scalable Data Processing and Machine Learning Pipeline

## Overview
This project demonstrates a scalable data processing and machine learning pipeline using Python, PyTorch, PostgreSQL, Spark, Hadoop, Docker, Kubernetes, AWS, Redis, and Kafka. It handles data ingestion, preprocessing, model training, and deployment for real-time predictions.

## Features
- Data ingestion with Kafka and preprocessing with Hadoop and Spark
- Machine learning model training with PyTorch
- Real-time model serving with Flask API and Redis caching
- Containerization with Docker
- Orchestration with Kubernetes
- Deployment on AWS
- Logging and monitoring with Prometheus

## Project Structure
- `data_ingestion/`: Scripts for data ingestion and preprocessing
- `ml_training/`: Scripts for model training and registry
- `model_serving/`: Flask API for model serving
- `deployment/`: Docker and Kubernetes configurations
- `config/`: Configuration files
- `monitoring/`: Logging and monitoring configurations
- `tests/`: Unit and integration tests
- `scripts/`: Setup and execution scripts

## Setup
1. Clone the repository:
```sh
git clone https://github.com/lomichael/data-ml-pipeline.git
cd data-ml-pipeline
```

2. Set up the environment:
```sh
source scripts/setup_env.sh
```

3. Install the necessary Python packages if not installed:
```sh
pip install kafka-python hdfs pyspark torch flask optuna redis
```

## Running the Pipeline
1. Run data ingestion and preprocessing:
```sh
python data_ingestion/kafka/kafka_producer.py
python data_ingestion/kafka/kafka_consumer.py
python data_ingestion/hadoop/ingest_data.py
python data_ingestion/hadoop/process_data.py
python data_ingestion/spark/preprocess_data.py
```

2. Train the machine learning model:
```sh
python ml_training/models/train.py
python ml_training/models/hyperparameter_tuning.py
python ml_training/registry/save_model.py
```

3. Deploy the Flask API:
```sh
docker build -t ml-api model_serving/
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
```

4. Start Redis Server:
``sh
sudo service redis-server start
```

5. Upload data to S3:
```sh
aws s3 cp /path/to/local/data s3://my-ml-pipeline-bucket/data --recursive
```

6. Start monitoring the pipeline:
```sh
prometheus --config.file=monitoring/metrics/prometheus_config.yaml
```

## License
This project is licensed under the MIT License.
