resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.inference_lambda.function_name}"
  retention_in_days = 14
}

resource "aws_cloudwatch_log_group" "sagemaker_log_group" {
  name              = "/aws/sagemaker/${aws_sagemaker_notebook_instance.mlops_notebook.name}"
  retention_in_days = 14
}
