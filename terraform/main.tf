variable "master_username" {}
variable "master_password" {}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "13.4"
  instance_class       = "db.t3.micro"
  db_name              = "pokecards_db"
  identifier           = "pokecards-dev-db"
  username             = var.master_username
  password             = var.master_password
  parameter_group_name = "default.postgres13"
  skip_final_snapshot  = true
  publicly_accessible  = false
}
