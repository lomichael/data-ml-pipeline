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
- `monitoring/`: Logging and monitoring configurations
- `tests/`: Unit and integration tests
- `scripts/`: Setup and execution scripts
- `config/`: Configuration files

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

3. Run the pipeline:
```sh
source scripts/run_pipeline.sh
```

## License
This project is licensed under the MIT License.
