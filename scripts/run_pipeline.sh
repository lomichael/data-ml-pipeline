#!/bin/bash

# Ensure necessary directories exist in HDFS
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -mkdir -p /user/hadoopuser/input
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -mkdir -p /data

# Create placeholder data in HDFS (if no real data available)
echo '{"name": "test", "value": 1}' > /tmp/datafile
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfs -put /tmp/datafile /user/hadoopuser/input/datafile

# Ensure DataNode is running
DATANODE_RUNNING=$(jps | grep DataNode)
if [ -z "$DATANODE_RUNNING" ]; then
  sudo -u hadoopuser /usr/local/hadoop/sbin/start-dfs.sh
  sudo -u hadoopuser /usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
fi

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
minikube start --driver=docker
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml

