resource "aws_sagemaker_notebook_instance" "mlops_notebook" {
  name           = var.notebook_instance_name
  instance_type  = var.notebook_instance_type
  role_arn       = aws_iam_role.sagemaker_execution_role.arn
}

resource "aws_sagemaker_pipeline" "mlops_pipeline" {
  pipeline_name = var.pipeline_name
  pipeline_display_name = var.pipeline_display_name       # Human-readable display name
  role_arn         = aws_iam_role.sagemaker_execution_role.arn # IAM Role ARN for execution
  pipeline_definition = file("${path.module}/sagemaker_pipeline.json")
}

resource "aws_sagemaker_endpoint" "inference_endpoint" {
  endpoint_config_name = aws_sagemaker_endpoint_configuration.inference_config.name
}
