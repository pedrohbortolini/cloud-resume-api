terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "chunk2-crc"
    key    = "cloudresume/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.region
}
