resource "digitalocean_ssh_key" "mint_marketing_ssh_key" {
  name       = "mint-marketing"
  public_key = file("~/.ssh/mint-marketing.pub")
}

resource "digitalocean_droplet" "mint_marketing_droplet" {
  image              = "ubuntu-18-04-x64"
  name               = "mint-marketing"
  tags               = ["mint-marketing"]
  region             = "lon1"
  size               = "s-1vcpu-1gb"
  private_networking = "true"
  ssh_keys           = [digitalocean_ssh_key.mint_marketing_ssh_key.fingerprint]
  depends_on         = [digitalocean_ssh_key.mint_marketing_ssh_key]
}

resource "digitalocean_domain" "mint_marketing_domain" {
  name       = "mintfiles.co.za"
  ip_address = digitalocean_droplet.mint_marketing_droplet.ipv4_address
  depends_on = [digitalocean_droplet.mint_marketing_droplet]
}

resource "digitalocean_project" "mint_marketing_project" {
  name        = "Mint marketing"
  description = "Mint marketing resources"
  purpose     = "Web Application"
  environment = "Production"
  resources   = [digitalocean_droplet.mint_marketing_droplet.urn]
  depends_on = [digitalocean_droplet.mint_marketing_droplet]
}
