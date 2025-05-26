# creating a vpc and its stacks


resource "aws_vpc" "rofiats_terraform_vpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "rofiats_terraform_vpc"
  }
}


resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.rofiats_terraform_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "private_subnet"
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.rofiats_terraform_vpc.id
  cidr_block = "10.0.2.0/24"

  tags = {
    Name = "public_subnet"
  }
}

resource "aws_internet_gateway" "rofi-igw" {
  vpc_id = aws_vpc.rofiats_terraform_vpc.id

  tags = {
    Name = "rofi-igw"
  }
}

# route_table 
resource "aws_route_table" "public_rofi_rt" {
  vpc_id = aws_vpc.rofiats_terraform_vpc.id

  tags = {
    Name = "public_rofi_rt"
  }
}

#route
resource "aws_route" "rofi_route" {
  route_table_id            = aws_route_table.public_rofi_rt.id
  destination_cidr_block    = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.rofi-igw.id
}

resource "aws_route_table_association" "associate_dem" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rofi_rt.id
}

#security group
resource "aws_security_group" "allow_traffic" {
  name        = "allow_traffic"
  description = "Allow inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.rofiats_terraform_vpc.id

  tags = {
    Name = "allow_traffic"
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh" {
  security_group_id = aws_security_group.allow_traffic.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.allow_traffic.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports,allow all types of ip-protocol
}
