provider "aws" {
  region = var.region
}

provider "aws" {
  alias  = "useast1"
  region = "us-east-1"
}