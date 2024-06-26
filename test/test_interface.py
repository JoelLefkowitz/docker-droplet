#!/usr/bin/env python
import os
import sys
import unittest
from subprocess import CalledProcessError, check_output

sys.path.append("..")


class TestInterface(unittest.TestCase):
    fixture_key = os.path.abspath("./src/tests/fixtures/steve.pub")

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
    check_output(call, cwd="src")


if __name__ == "__main__":
    unittest.main()
