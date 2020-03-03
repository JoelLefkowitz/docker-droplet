import subprocess
from setuptools import find_packages, setup
from distutils.core import Command

__version__ = "1.0.8"

with open("README.md", "r") as f:
    long_description = f.read()


class UpdateDocs(Command):
    description = "Update build configuration using sphinx-apidoc"
    user_options = []

    def initialize_options(self) -> None:
        self.version = __version__

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-apidoc", "-o", "docs/", "src/", "tests/"])


class GenerateDocs(Command):
    description = "Generate docs using sphinx-autodoc"
    user_options = []

    def initialize_options(self) -> None:
        self.version = __version__

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-build", "docs/", "build/"])


s = setup(
    name="docker-droplet",
    version=__version__,
    license="MIT",
    description="Create a single digital ocean droplet and provision it to run the docker engine over a simple cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/docker-droplet",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "docopts>=0.6.1",
        "ansible>=2.8.0",
        "jinja2>=2.11.1",
        "doboto>=0.6.1",
    ],
    entry_points={"console_scripts": ["docker-droplet=docker_droplet.main:main"]},
    cmdclass={"updateDocs": UpdateDocs, "generateDocs": GenerateDocs},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
