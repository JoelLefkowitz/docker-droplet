import os
from subprocess import run


def tear_down(_, config_path) -> None:
    """
    Destroys the terraform infrastructure specified in the config path provided.

    Args:
        token ([type]): Digitalocean access token
        config_path ([type]): Terraform config path
    """
    run(["terraform", "destroy"], cwd=os.path.dirname(config_path), check=False)
