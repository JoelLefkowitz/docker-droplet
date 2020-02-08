# docker-droplet
Create a single digital ocean droplet and provision it to run the docker engine over a simple cli.

## Status

| Source  | Shields  |
|-----|--------------|
| Project  | ![license][license] ![release][release]  |
| Publishers  | [![pypi][pypi]][pypi_link]    |
| Downloads  | ![pypi_downloads][pypi_downloads] |
| Raised  | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link]  |

[license]: https://img.shields.io/github/license/joellefkowitz/docker-droplet

[release]: https://img.shields.io/github/v/release/joellefkowitz/docker-droplet

[pypi]: https://img.shields.io/pypi/v/docker-droplet (PyPi)
[pypi_link]: https://pypi.org/project/docker-droplet

[python_version]: https://img.shields.io/pypi/pyversions/docker-droplet

[pypi_downloads]: https://img.shields.io/pypi/dw/docker-droplet

[issues]: https://img.shields.io/github/issues/joellefkowitz/docker-droplet (Issues)
[issues_link]: https://github.com/JoelLefkowitz/docker-droplet/issues

[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/docker-droplet (Pull requests)
[pulls_link]: https://github.com/JoelLefkowitz/docker-droplet/pulls  

## Motivation

Creating a single droplet provisioned to use docker should be quick. Ansible and Terraform are the appropriate tools but may take long to configure for a single droplet. This package provides a simple cli to streamline the use of these tools.

### Installing

Install from pypi:

```bash
pip install docker-droplet
```

## Running the app

```bash
Usage:
   docker-droplet up [options]
   docker-droplet down [options]
```

To create a terraform configuration and run an ansible playbook to install docker:
```bash
docker-droplet up --droplet-name steve --ssh-key /home/.ssh/steve.pub --token 12345 --config-path /Workspace/config.tf
```
Where the terraform configuration path defaults to "./config.tf"

The droplet's name, ssh key path and digitalocean token can be given as environmnet variables:
```bash
export TF_VAR_DOCKER_DROPLET_DROPLET_NAME=steve
export TF_VAR_DOCKER_DROPLET_SSH_KEY=/home/.ssh/steve.pub
export TF_VAR_DOCKER_DROPLET_TOKEN=12345
docker-droplet up
```

A domain and digital ocean project title can also be included
```bash
docker-droplet up --domain example.com --project example
```

To remove the structure simply take it down:
```bash
docker-droplet down --token 12345 --config-path /Workspace/config.tf
```

## Running tests

Under development

### What is being tested

Under development

## Docs

Under development

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository.

## Author

* **Joel Lefkowitz** - *Initial work* - [JoelLefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

None
