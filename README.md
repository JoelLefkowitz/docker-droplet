# Docker droplet

Create a single digital ocean droplet and provision it to run the docker engine over a simple cli.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/docker-droplet/review.yml)
![Version](https://img.shields.io/pypi/v/docker-droplet)
![Downloads](https://img.shields.io/pypi/dw/docker-droplet)
![Quality](https://img.shields.io/codacy/grade/8f8992dd03d54b68b23c9e3879db7f86)
![Coverage](https://img.shields.io/codacy/coverage/8f8992dd03d54b68b23c9e3879db7f86)

## Installation

```bash
pip install docker-droplet
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/docker-droplet).

## Usage

```bash
Usage:
   docker-droplet up [options]
   docker-droplet down [options]
```

To create a terraform configuration and run an ansible playbook to install docker:

```bash
docker-droplet up --droplet-name steve --ssh-key /home/.ssh/steve.pub --token 12345 --config-path /Workspace/config.tf
```

The terraform configuration path defaults to "./config.tf"

The droplet's name, ssh key path and digitalocean token will be synchronized with environment variables:

```bash
export TF_VAR_DOCKER_DROPLET_DROPLET_NAME=steve
export TF_VAR_DOCKER_DROPLET_SSH_KEY=/home/.ssh/steve.pub
export TF_VAR_DOCKER_DROPLET_TOKEN=12345
docker-droplet up
```

A domain and digital ocean project title can also be specified

```bash
docker-droplet up --domain example.com --project example
```

To remove the structure simply take it down:

```bash
docker-droplet down --token 12345 --config-path /Workspace/config.tf
```

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
