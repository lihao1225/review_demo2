import json
import os

import requests

from demo6.common.handle_path import Data
from demo6.common.handle_yaml import HandleYaml
from demo6.common.myconfig import conf


class BaseApi():
    # file_path = os.path.join(Data, "env.yaml")
    # host = HandleYaml().read_yaml(file_path)["env"]["host"]
    param = {}
    param["host"] = conf.get("env","host")

    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.param.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        return requests.request(**data).json()
