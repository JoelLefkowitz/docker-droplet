variable "DOCKER_DROPLET_TOKEN" {} 

provider "digitalocean" {
  token = var.DOCKER_DROPLET_TOKEN
}

resource "digitalocean_ssh_key" "auto_ssh_key" {
  name       = "mydrop-ssh-key"
  public_key = file("/home/joel/.ssh/practice0.pub")
}

resource "digitalocean_droplet" "auto_droplet" {
  image              = "ubuntu-18-04-x64"
  name               = "mydrop"
  tags               = ["mydrop"]
  region             = "lon1"
  size               = "s-1vcpu-1gb"
  private_networking = "true"
  ssh_keys           = [digitalocean_ssh_key.auto_ssh_key.fingerprint]
  depends_on         = [digitalocean_ssh_key.auto_ssh_key]
}

