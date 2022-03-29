terraform {
  backend "s3" {
    bucket = "tjth-states-827047072822"
    key    = "readme.state"
    region = "eu-west-1"
  }
}