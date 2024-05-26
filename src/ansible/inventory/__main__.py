#!/usr/bin/env python
import json
import os
from doboto.DO import DO


def main() -> None:
    """
    Dynamic inventory script for Digitalocean. Targets a single specified
    droplet. Gets access token and droplet name from environment variables.
    """

    token = os.environ.get("TF_VAR_DOCKER_DROPLET_TOKEN")
    name = os.environ.get("TF_VAR_DOCKER_DROPLET_DROPLET_NAME")

    client = DO(token=token)
    hosts = [
        d["networks"]["v4"][0]["ip_address"]
        for d in client.droplet.list()
        if d["name"] == name
    ]

    # Terraform creates them in this order
    hosts.reverse()

    print(
        json.dumps(
            {
                "_meta": {"hostvars": {}},
                "instances": {
                    "hosts": hosts,
                    "vars": {},
                },
            }
        )
    )


if __name__ == "__main__":
    main()
