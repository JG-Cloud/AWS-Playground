terraform {
  backend "s3" {
    bucket = "jg-playground"
    key    = "aws-playground-terraform.tfstate"
    region = "eu-west-1"
    encrypt= "true"
  }
}

