resource "aws_s3_bucket" "food50_bucket" {
  bucket = var.s3_bucket_name

  tags = {
    Name        = "food50-bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.food50_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.food50_bucket.bucket
}