# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "3.7.2"
    }
  }
}

provider "random" {
  # Configuration options
}