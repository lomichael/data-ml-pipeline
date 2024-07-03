#!/bin/bash

# Update and install dependencies
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Install kubectl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt-get update
sudo apt-get install -y kubectl

# Install AWS CLI
sudo apt-get install -y awscli

# Configure Kubernetes to use AWS
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

# Install eksctl for EKS cluster management
curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/0.48.0/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

# Install Redis
sudo apt-get install -y redis-server
sudo systemctl enable redis-server.service

echo "Setup complete"

