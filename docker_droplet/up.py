from os.path import abspath, dirname
from subprocess import run

from terraform.template import create_config


def set_up(droplet_name, ssh_key, token, project, domain, config_path):

    with open(config_path, "w") as config_file:
        config_text = create_config(droplet_name, ssh_key, project, domain)
        config_file.write(config_text)

    run(["terraform", "init"], cwd=dirname(config_path))
    run(["terraform", "apply"], cwd=dirname(config_path))

    INVENTORY = abspath("./ansible/inventory")
    PLAYBOOK = abspath("./ansible/playbook.yml")
    run(["ansible-playbook", "-i", INVENTORY, PLAYBOOK, "-u", "root"])
