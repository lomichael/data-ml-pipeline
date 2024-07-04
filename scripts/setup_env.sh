#!/bin/bash

# Update and install dependencies
sudo apt-get update
sudo apt-get install -y openjdk-11-jdk python3-pip git docker.io

# Install Kubernetes and Minikube
sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
sudo mv minikube /usr/local/bin/

# Install Redis
sudo apt-get install -y redis-server
sudo systemctl enable redis-server
sudo systemctl start redis-server

# Install PostgreSQL
sudo apt-get install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo -u postgres psql -c "CREATE DATABASE ml_pipeline;"
sudo -u postgres psql -c "CREATE USER postgres WITH PASSWORD 'your_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ml_pipeline TO postgres;"

# Install Kafka
wget https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xzf kafka_2.13-3.7.0.tgz
mv kafka_2.13-3.7.0 kafka

# Install Hadoop
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzvf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop

# Install Spark
wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar -xzvf spark-3.5.1-bin-hadoop3.tgz
sudo mv spark-3.5.1-bin-hadoop3 /usr/local/spark

# Install Python packages
pip3 install kafka-python hdfs pyspark torch flask optuna redis psycopg2-binary

# Set environment variables
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> ~/.bashrc
echo "export HADOOP_HOME=/usr/local/hadoop" >> ~/.bashrc
echo "export PATH=\$PATH:\$JAVA_HOME/bin:\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin:/usr/local/spark/bin" >> ~/.bashrc
source ~/.bashrc

# Enable Docker BuildKit
export DOCKER_BUILDKIT=1
docker buildx create --use

# Format Namenode
sudo -u hadoopuser /usr/local/hadoop/bin/hdfs namenode -format

# Start Hadoop services
sudo -u hadoopuser /usr/local/hadoop/sbin/start-dfs.sh
sudo -u hadoopuser /usr/local/hadoop/sbin/start-yarn.sh

# Start Kafka and ZooKeeper
cd kafka
nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties > zookeeper.log 2>&1 &
nohup ./bin/kafka-server-start.sh config/server.properties > kafka.log 2>&1 &

