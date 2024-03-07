data "aws_vpc" "main_prod_vpc" {
  filter {
    name   = "tag:Name"
    values = ["main_prod_vpc"]
  }
}