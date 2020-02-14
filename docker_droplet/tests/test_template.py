import unittest
import pathlib
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound


class TestTemplate(unittest.TestCase):
    def test_loader(self) -> None:
        directory = pathlib.Path("docker_droplet/terraform/").absolute()
        templateLoader = FileSystemLoader(searchpath=directory)
        templateEnv = Environment(loader=templateLoader)

        try:
            templateEnv.get_template("providers.jinja2")
            templateEnv.get_template("digitalocean.jinja2")
        except TemplateNotFound:
            self.fail("Jinja templates not found")


if __name__ == "__main__":
    unittest.main()
