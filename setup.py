from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

s = setup(
    name="docker-droplet",
    version="0.1.1",
    license="MIT",
    description="Create a single digital ocean droplet and provision it to run the docker engine over a simple cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/docker-droplet",
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "docopts>=0.6.1",
        "ansible>=2.8.0",
        "jinja2>=2.11.1",
        "doboto>=0.6.1",
    ],
    entry_points={"console_scripts": ["docker-droplet=docker_droplet.main:main"]},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
