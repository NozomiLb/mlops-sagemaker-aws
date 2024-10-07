#!/bin/bash

# Define repository and image name
repo_name="your-ecr-repo"
image_name="cnn-model-inference"
region="us-west-2"
account_id=$(aws sts get-caller-identity --query Account --output text)

# Build Docker image
docker build -t $image_name .

# Tag the image
docker tag $image_name:latest $account_id.dkr.ecr.$region.amazonaws.com/$repo_name:$image_name

# Log in to ECR
aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $account_id.dkr.ecr.$region.amazonaws.com

# Push the image to ECR
docker push $account_id.dkr.ecr.$region.amazonaws.com/$repo_name:$image_name

echo "Docker image pushed to ECR: $account_id.dkr.ecr.$region.amazonaws.com/$repo_name:$image_name"