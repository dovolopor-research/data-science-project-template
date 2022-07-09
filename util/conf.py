from typing import Optional
from os import environ

from ruamel.yaml import YAML

from util.data_model import Env

ENV = environ.get("ENV", Env.DEV)
print(f">> current env: {ENV.value}")
yaml = YAML()


def read_yaml(yaml_path: str) -> dict:
    with open(yaml_path, "r") as f_yaml:
        datas = yaml.load(f_yaml)
    return datas


def get_conf(conf_path: Optional[str] = None) -> dict:
    if conf_path is None:
        try:
            env = Env(ENV)
        except ValueError as e:
            raise e

        if env == Env.DEV:
            conf_path = "./conf/default.yml"
        else:
            conf_path = f"./conf/default.{env.value}.yml"

    conf = read_yaml(conf_path)
    conf["env"] = ENV.value
    return conf
