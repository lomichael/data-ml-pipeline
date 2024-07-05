#!/bin/bash

# Ensure necessary directories exist in HDFS
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -mkdir -p /user/hadoopuser/input
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -mkdir -p /data

# Upload test data to HDFS (assuming you have local test data files)
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -put /path/to/your/local/datafile /user/hadoopuser/input/datafile
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -put /path/to/your/local/kafka_data.json /data/kafka_data.json

# Run data ingestion and preprocessing scripts
python3 data_ingestion/kafka/kafka_producer.py &
python3 data_ingestion/kafka/kafka_consumer.py &
python3 data_ingestion/hadoop/ingest_data.py
python3 data_ingestion/hadoop/process_data.py
python3 data_ingestion/spark/preprocess_data.py

# Train the machine learning model
python3 ml_training/models/train.py

# Hyperparameter tuning
python3 ml_training/models/hyperparameter_tuning.py

# Save the model
python3 ml_training/registry/save_model.py

# Build and run Docker container for Flask API
cd model_serving
docker build -t ml-api .
docker run -p 5000:5000 ml-api

# Deploy with Kubernetes
minikube start
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml

