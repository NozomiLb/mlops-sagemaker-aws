resource "aws_api_gateway_rest_api" "inference_api" {
  name        = "InferenceAPI"
  description = "API for inference"
}

resource "aws_api_gateway_resource" "root_resource" {
  rest_api_id = aws_api_gateway_rest_api.inference_api.id
  parent_id   = aws_api_gateway_rest_api.inference_api.root_resource_id
  path_part   = "inference"
}

resource "aws_api_gateway_method" "post_method" {
  rest_api_id   = aws_api_gateway_rest_api.inference_api.id
  resource_id   = aws_api_gateway_resource.root_resource.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id            = aws_api_gateway_rest_api.inference_api.id
  resource_id            = aws_api_gateway_resource.root_resource.id
  http_method            = aws_api_gateway_method.post_method.http_method
  integration_http_method = "POST"
  type                   = "AWS_PROXY"
}
