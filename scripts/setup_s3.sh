#!/bin/bash

# Create an S3 bucket
aws s3api create-bucket --bucket my-ml-pipeline-bucket --region us-west-2

# Upload data to S3
aws s3 cp /path/to/local/data s3://my-ml-pipeline-bucket/data --recursive

