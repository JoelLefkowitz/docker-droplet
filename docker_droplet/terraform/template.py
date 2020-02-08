import pathlib
from jinja2 import Environment, FileSystemLoader


def create_config(droplet_name, ssh_key, project, domain) -> str:
    directory = pathlib.Path(__file__).parent.absolute()
    templateLoader = FileSystemLoader(searchpath=directory)
    templateEnv = Environment(loader=templateLoader)

    providers_template = templateEnv.get_template("providers.jinja2")
    resources_template = templateEnv.get_template("digitalocean.jinja2")

    providers_config = providers_template.render()
    resources_config = resources_template.render(
        droplet_name=droplet_name, ssh_key=ssh_key, project=project, domain=domain
    )
    return "\n\n".join([providers_config, resources_config])
