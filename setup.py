"""
Setup script for docker-droplet
"""

from setuptools import find_packages, setup
from distutils.core import setup, Command
from unittest import TestLoader, TextTestRunner
from sphinx.setup_command import BuildDoc

__version__ = "1.0.1"


class DocsCommand(BuildDoc):
    description = "Generate build configuration and make docs"

    def initialize_options(self) -> None:
        """  
        Docs command override. Call the parent initializer then add version and config directory
        """
        super().initialize_options()
        self.version = __version__
        self.config_dir = "./docker_droplet/docs"


class TestsCommand(Command):
    description = "Discover and run tests"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        """
        Discover and run tests        
        """
        suite = TestLoader().discover("./docker_droplet/tests")
        TextTestRunner().run(suite)


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="docker-droplet",
    version=__version__,
    license="MIT",
    description="Create a single digital ocean droplet and provision it to run the docker engine over a simple cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/docker-droplet",
    include_package_data=True,
    package_data={"": ["**/*yml", "**/*.jinja2"]},
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "docopts>=0.6.1",
        "ansible>=2.8.0",
        "jinja2>=2.11.1",
        "doboto>=0.6.1",
        "sphinx>=2.4.1"
    ],
    entry_points={"console_scripts": ["docker-droplet=docker_droplet.main:main"]},
    cmdclass={"docs": DocsCommand, "test": TestsCommand},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
