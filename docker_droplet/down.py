from os.path import dirname
from subprocess import run


def tear_down(token, config_path) -> None:
    """
    Destroys the terraform infrastructure specified in the config path provided.
    
    Args:
        token ([type]): Digitalocean access token
        config_path ([type]): Terraform config path
    """
    run(["terraform", "destroy"], cwd=dirname(config_path))
