resource "aws_dynamodb_table" "calorie_table" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "food_id"

  attribute {
    name = "food_id"
    type = "S"
  }
}
