#!/bin/bash

# Define model and endpoint variables
model_name="cnn-model"
endpoint_config_name="cnn-model-endpoint-config"
endpoint_name="cnn-model-endpoint"
region="us-east-1"

# Create Model
aws sagemaker create-model \
  --model-name $model_name \
  --primary-container Image="763104351884.dkr.ecr.$region.amazonaws.com/tensorflow-inference:2.3-gpu-py37-ubuntu18.04",ModelDataUrl="s3://your-bucket/output/model.tar.gz" \
  --execution-role-arn "arn:aws:iam::your-account-id:role/sagemaker-execution-role" \
  --region $region

# Create Endpoint Config
aws sagemaker create-endpoint-config \
  --endpoint-config-name $endpoint_config_name \
  --production-variants VariantName="cnnVariant",ModelName=$model_name,InitialInstanceCount=1,InstanceType="ml.m5.xlarge" \
  --region $region

# Create Endpoint
aws sagemaker create-endpoint \
  --endpoint-name $endpoint_name \
  --endpoint-config-name $endpoint_config_name \
  --region $region

echo "SageMaker endpoint $endpoint_name created!"