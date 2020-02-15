#!/usr/bin/env python3

"""
Entrypoint for docker-droplet
Parse command line arguments and call the selected handlers
"""

import sys
from os import getcwd, path, environ
from inspect import cleandoc
from os.path import dirname, exists

from docopt import docopt  # type: ignore

# If packaged multi_job will be scoped, otherwise append parent path.
package_directory = path.realpath(path.join(__file__, "../.."))
sys.path.append(package_directory)

from docker_droplet.down import tear_down
from docker_droplet.exceptions import MissingVariable, PathNotResolvable
from docker_droplet.up import set_up

CLI = cleandoc(
    """
    Usage:
       docker-droplet up [options]
       docker-droplet down [options]
    
    Options:
       --droplet-name=<name>
       --ssh-key=<ssh-key>
       --token=<token>
       --project=<project>
       --domain=<domain>
       --config-path=<config-path>"""
)


class InputArg:
    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = None if value == "None" else value

    def assign_default(self, default: str) -> None:
        """
        If the object's value attribute is None the assign a default value
        
        Args:
            default (str): 
        """
        if not self.value:
            self.value = default

    def validate_path(self, check_file_exists: bool = False) -> None:
        """
        Check if path's directory is resolvable. Optionally check if the path itself exists.
        
        Args:
            check_file_exists (bool, optional): [description]. Defaults to False.
        
        Raises:
            PathNotResolvable: [description]
            PathNotResolvable: [description]
        """
        if not path.exists(path.dirname(self.value)):
            raise PathNotResolvable(self.name, self.value)

        if check_file_exists and not path.exists(self.value):
            raise PathNotResolvable(self.name, self.value)

    def sync_env(self) -> None:
        """
        Synchronize the object's value with the environment variable TF_VAR_<name>
        """
        NAME = "TF_VAR_DOCKER_DROPLET_" + self.name.upper()
        if self.value:
            environ.putenv(NAME, self.value)
        else:
            self.value = environ.get(NAME, None)

    def set_required(self) -> None:
        if not self.value:
            raise MissingVariable(self.name)

    def __str__(self) -> str:
        return f"{self.name}: {self.value}"


def main() -> None:
    """
    Entry point for docker-droplet
    """
    arguments = docopt(CLI)
    droplet_name = InputArg("droplet_name", arguments["--droplet-name"])
    ssh_key = InputArg("ssh_key", arguments["--ssh-key"])
    token = InputArg("token", arguments["--token"])
    project = InputArg("project", arguments["--project"])
    domain = InputArg("domain", arguments["--domain"])
    config_path = InputArg("config_path", arguments["--config-path"])

    token.sync_env()
    token.set_required()

    if arguments["up"]:
        config_path.assign_default("./config.tf")
        config_path.validate_path()

        droplet_name.sync_env()
        droplet_name.set_required()

        ssh_key.sync_env()
        ssh_key.set_required()
        ssh_key.validate_path(check_file_exists=True)

        set_up(
            droplet_name.value,
            ssh_key.value,
            token.value,
            project.value,
            domain.value,
            config_path.value,
        )

    if arguments["down"]:
        config_path.set_required()
        config_path.validate_path()
        tear_down(token.value, config_path.value)


if __name__ == "__main__":
    main()
