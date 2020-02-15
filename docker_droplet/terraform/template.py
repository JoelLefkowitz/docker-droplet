from os import path
from jinja2 import Environment, FileSystemLoader


def create_config(droplet_name, ssh_key, project, domain) -> str:
    """
    Create a terraform configuration file for a single droplet
    
    Args:
        droplet_name ([type]): 
        ssh_key ([type]):
        project ([type]):
        domain ([type]):
    
    Returns:
        str: Configuration file as a string
    """
    directory = path.realpath(path.join(__file__, ".."))
    templateLoader = FileSystemLoader(searchpath=directory)
    templateEnv = Environment(loader=templateLoader)

    print(templateEnv)

    providers_template = templateEnv.get_template("providers.jinja2")
    resources_template = templateEnv.get_template("digitalocean.jinja2")

    providers_config = providers_template.render()
    resources_config = resources_template.render(
        droplet_name=droplet_name, ssh_key=ssh_key, project=project, domain=domain
    )
    return "\n\n".join([providers_config, resources_config])
