# Docker droplet

Create a single digital ocean droplet and provision it to run the docker engine over a simple cli.

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield] ![dependents][dependents_shield]                             |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Installation

```bash
pip install docker-droplet
```

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

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/docker-droplet/pulls
[issues]: https://github.com/JoelLefkowitz/docker-droplet/issues

<!-- External links -->

[readthedocs]: https://docker-droplet.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/docker-droplet
[license_shield]: https://img.shields.io/github/license/joellefkowitz/docker-droplet
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/docker-droplet

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/docker-droplet
[codacy_shield]: https://img.shields.io/codacy/coverage/docker-droplet
[coverage_shield]: https://img.shields.io/codacy/grade/docker-droplet
[readthedocs_shield]: https://img.shields.io/readthedocs/docker-droplet

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/docker-droplet
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/docker-droplet

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/docker-droplet
[python_versions_shield]: https://img.shields.io/pypi/pyversions/docker-droplet
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/docker-droplet

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/docker-droplet
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/docker-droplet
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/docker-droplet
