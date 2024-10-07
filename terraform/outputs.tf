output "api_gateway_url" {
  description = "URL of the API Gateway"
  value       = aws_api_gateway_rest_api.inference_api.execution_arn
}

output "sagemaker_endpoint_url" {
  description = "SageMaker Endpoint for model inference"
  value       = aws_sagemaker_endpoint.inference_endpoint.endpoint_config_name
}

output "dynamodb_table_name" {
  description = "DynamoDB Table for storing calorie data"
  value       = aws_dynamodb_table.calorie_table.name
}
