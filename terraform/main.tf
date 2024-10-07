terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
}

# Load all resources from separate files
module "s3" {
  source = "./s3.tf"
}

module "sagemaker" {
  source = "./sagemaker.tf"
}

module "dynamodb" {
  source = "./dynamodb.tf"
}

module "lambda" {
  source = "./lambda.tf"
}

module "api_gateway" {
  source = "./api_gateway.tf"
}

module "cloudwatch" {
  source = "./cloudwatch.tf"
}

module "iam" {
  source = "./iam.tf"
}