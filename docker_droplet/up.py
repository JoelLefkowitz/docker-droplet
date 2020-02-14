import pathlib
from os import chmod, stat
from os.path import dirname, join
from stat import S_IEXEC
from subprocess import run


import sys

sys.path.append("..")
from docker_droplet.terraform.template import create_config


def set_up(droplet_name, ssh_key, token, project, domain, config_path) -> None:
    """ 
    Call functions to create a terraform configuration and then provision the infrastructure with an ansible playbook.
    
    Args:
        droplet_name ([type]):
        ssh_key ([type]):
        token ([type]):
        project ([type]):
        domain ([type]):
        config_path ([type]):
    """

    # Create config from template
    with open(config_path, "w") as config_file:
        config_text = create_config(droplet_name, ssh_key, project, domain)
        config_file.write(config_text)

    # Run terraform from config directory
    run(["terraform", "init"], cwd=dirname(config_path))
    run(["terraform", "apply"], cwd=dirname(config_path))

    # Define ansible paths
    directory = pathlib.Path(__file__).parent.absolute()
    INVENTORY = join(directory, "ansible/inventory")
    INVENTORY_SCRIPT = join(INVENTORY, "digitalocean.py")
    PLAYBOOK = join(directory, "ansible/playbook.yml")

    # Make sure dynamic inventory script is executable
    chmod(INVENTORY_SCRIPT, stat(INVENTORY_SCRIPT).st_mode | S_IEXEC)

    # Provision the droplet
    run(["ansible-playbook", "-i", INVENTORY, PLAYBOOK, "-u", "root"])
