from os.path import abspath, dirname
from subprocess import run


def tear_down(token, config_path):
    run(["terraform", "destroy"], cwd=dirname(config_path))

