#!/usr/bin/env python
import json
from doboto.DO import DO


def main():
    client = DO(
        token=""
    )
    hosts = []

    for d in client.droplet.list():
        public_network = d["networks"]["v4"][0]
        hosts.append(public_network["ip_address"])

    # Terraform creates them in this order
    hosts.reverse()

    print(
        json.dumps(
            {"_meta": {"hostvars": {}}, "instances": {"hosts": hosts, "vars": {},},}
        )
    )


if __name__ == "__main__":
    main()
