# Deep Learning Project for Meal Detection and Calorie Estimation with an Automated MLOps Pipeline using AWS SageMaker

This repository contains an end-to-end MLOps pipeline for training, deploying, and maintaining a food image classification model with calorie estimation in AWS SageMaker. The project uses AWS SageMaker, Lambda, API Gateway, DynamoDB, and other AWS services, integrated with CI/CD pipelines for automation.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Setup](#setup)
- [Training the Model](#training-the-model)
- [Deploying the Model](#deploying-the-model)
- [Calorie Lookup Service](#calorie-lookup-service)
- [CI/CD Pipeline](#cicd-pipeline)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements a deep learning-based food classification model that detects food items from images and estimates their calorie content by looking up the nutritional data stored in DynamoDB. It also includes MLOps practices to automate model retraining and deployment using Terraform, Docker, and GitLab CI/CD.

Key technologies and tools:
- **AWS SageMaker**: For model training, deployment, and inference.
- **Amazon S3**: For storing datasets and model artifacts.
- **DynamoDB**: For storing nutritional data.
- **Lambda & API Gateway**: For serving predictions and calorie estimations.
- **Terraform**: For managing AWS infrastructure.
- **GitLab CI/CD**: For continuous integration and deployment pipelines.

## Architecture

The diagram below shows the architecture of the project:

![Project Architecture](path-to-your-architecture-image.png)

1. **S3**: Stores training and test data.
2. **SageMaker**: Trains the model and deploys the inference endpoint.
3. **Lambda & API Gateway**: Expose the model as an API for predictions.
4. **DynamoDB**: Stores calorie information for food items.
5. **CI/CD**: Automated retraining, testing, and deployment with GitLab CI/CD.
6. **Terraform**: Automates the creation of AWS resources.
7. **CloudWatch**: For monitoring the model and system metrics.

## Setup

### Prerequisites

To run this project, you'll need:
- An AWS account with permissions to use SageMaker, Lambda, API Gateway, S3, and DynamoDB.
- Docker installed on your local machine.
- Terraform installed for infrastructure automation.
- A GitLab account with CI/CD pipelines configured.