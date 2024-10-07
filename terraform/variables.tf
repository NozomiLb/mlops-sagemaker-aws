variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "notebook_instance_name" {
  description = "Name for the SageMaker Notebook instance"
  type        = string
  default     = "mlops-notebook-instance"
}

variable "notebook_instance_type" {
  description = "Instance type for SageMaker Notebook"
  type        = string
  default     = "ml.t2.medium"
}

variable "pipeline_name" {
  description = "Name of the SageMaker pipeline"
  type        = string
  default     = "mlops-sagemaker-pipeline"
}

variable "pipeline_display_name" {
  description = "A user-friendly display name for the SageMaker MLOps pipeline"
  type        = string
  default = "MLOps SageMaker Pipeline"
}

variable "sagemaker_endpoint_name" {
  description = "Name of the SageMaker endpoint for inference"
  type        = string
  default     = "mlops-inference-endpoint"
}

variable "dynamodb_table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "CalorieInfoTable"
}
