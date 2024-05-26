import os
import pathlib
import sys
from .terraform.template import create_config
from stat import S_IEXEC
from subprocess import run

sys.path.append("..")


def set_up(droplet_name, ssh_key, project, domain, config_path) -> None:
    """
    Call functions to create a terraform configuration and then provision the
    infrastructure with an ansible playbook.

    Args:
        droplet_name ([type]):
        ssh_key ([type]):
        project ([type]):
        domain ([type]):
        config_path ([type]):
    """

    # Create config from template
    with open(config_path, "w", encoding="utf8") as config_file:
        config_text = create_config(droplet_name, ssh_key, project, domain)
        config_file.write(config_text)

    # Run terraform from config directory
    run(["terraform", "init"], cwd=os.path.dirname(config_path), check=False)
    run(["terraform", "apply"], cwd=os.path.dirname(config_path), check=False)

    # Define ansible paths
    directory = pathlib.Path(__file__).parent.absolute()
    inventory = os.path.join(directory, "ansible/inventory")
    inventory_script = os.path.join(inventory, "digitalocean.py")
    playbook = os.path.join(directory, "ansible/playbook.yml")

    # Make sure dynamic inventory script is executable
    os.chmod(inventory_script, os.stat(inventory_script).st_mode | S_IEXEC)

    # Provision the droplet
    run(["ansible-playbook", "-i", inventory, playbook, "-u", "root"], check=False)
