import pathlib
from os.path import join, dirname
from subprocess import run

from docker_droplet.terraform.template import create_config


def set_up(droplet_name, ssh_key, token, project, domain, config_path):

    with open(config_path, "w") as config_file:
        config_text = create_config(droplet_name, ssh_key, project, domain)
        config_file.write(config_text)

    run(["terraform", "init"], cwd=dirname(config_path))
    run(["terraform", "apply"], cwd=dirname(config_path))

    directory = pathlib.Path(__file__).parent.absolute()
    INVENTORY = join(directory, "ansible/inventory")
    PLAYBOOK = join(directory, "ansible/playbook.yml")
    run(["ansible-playbook", "-i", INVENTORY, PLAYBOOK, "-u", "root"])
