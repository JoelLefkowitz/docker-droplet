import unittest
from os.path import abspath
from subprocess import check_output, CalledProcessError
from docopt import DocoptExit

import sys

sys.path.append("..")
from docker_droplet.exceptions import MissingVariable, PathNotResolvable


class TestInterface(unittest.TestCase):
    fixture_key = abspath("./docker_droplet/tests/fixtures/steve.pub")

    def test_bounce_empty(self) -> None:
        with self.assertRaises(CalledProcessError):
            call_interface()

    def test_path_validation(self) -> None:
        with self.assertRaises(CalledProcessError):
            call_interface(name="steve", ssh_key="99", token="12345")


def call_interface(name=None, ssh_key=None, token=None, config_path=None) -> None:
    call = ["python", "main.py", "up"]
    if name:
        call.append(f"--droplet-name={name}")
    if ssh_key:
        call.append(f"--ssh-key={ssh_key}")
    if token:
        call.append(f"--token={token}")
    if config_path:
        call.append(f"--config-path={config_path}")
    check_output(call, cwd="docker_droplet")


if __name__ == "__main__":
    unittest.main()
