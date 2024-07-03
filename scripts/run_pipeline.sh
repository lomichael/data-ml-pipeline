#!/bin/bash

# Run data ingestion
python data_ingestion/kafka/kafka_producer.py
python data_ingestion/kafka/kafka_consumer.py
python data_ingestion/hadoop/ingest_data.py
python data_ingestion/hadoop/process_data.py
python data_ingestion/spark/preprocess_data.py

# Train the model
python ml_training/models/train.py
python ml_training/models/hyperparameter_tuning.py
python ml_training/registry/save_model.py

# Deploy the model serving API
docker build -t ml-api model_serving/
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml

# Start Redis server
sudo service redis-server start

# Upload data to S3
aws s3 cp /path/to/local/data s3://my-ml-pipeline-bucket/data --recursive

# Start monitoring
prometheus --config.file=monitoring/metrics/prometheus_config.yaml

