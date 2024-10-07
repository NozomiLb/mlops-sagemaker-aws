resource "aws_lambda_function" "inference_lambda" {
  function_name = "inferenceLambda"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  filename      = "/data/lambda.zip"

  environment {
    variables = {
      SAGEMAKER_ENDPOINT = aws_sagemaker_endpoint.inference_endpoint.endpoint_config_name
    }
  }
}