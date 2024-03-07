terraform {
  backend "s3" {
    bucket = "terraform-states-miakito"
    key    = "${var.project_name}/state.tfstate"
    region = "eu-west-3"
    dynamodb_table = "terraform-state-smart-lock-table"
    encrypt = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  # provided by aws cli, or env variables
}

resource "aws_security_group" "ec2_security_group" {
  name        = "${var.project_name}_ec2_security_group"
  description = "Allow all inbound traffic"
  vpc_id      = data.aws_vpc.main_prod_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-01d21b7be69801c2f" # Canonical, Ubuntu, 22.04 LTS, amd64 jammy image build on 2023-12-07
  instance_type = "t2.micro"
  key_name      = "GITHUB_SSH_KEY"

  security_groups = [aws_security_group.ec2_security_group.name]
  tags = {
    Name = "${var.project_name}"
  }
}

