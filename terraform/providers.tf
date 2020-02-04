variable "DO_ACCESS_TOKEN" {} 

provider "digitalocean" {
  token = var.DO_ACCESS_TOKEN
}
