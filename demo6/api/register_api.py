import os

import yaml

from demo6.api.base_api import BaseApi
from demo6.common.handle_path import Data
from demo6.common.handle_yaml import HandleYaml


class RegisterApi(BaseApi):

    def __init__(self):
        file_path = os.path.join(Data, "api.yaml")
        self.data=HandleYaml().read_yaml(file_path)
        # with open(file_path, encoding="utf-8") as f:
        #     self.data = yaml.load(f)

    def register(self, mobile, pwd):
        self.param["mobile"] = mobile
        self.param["pwd"] = pwd

        return self.send(self.data["register"])

    def login(self, mobile, pwd):
        self.param["mobile"] = mobile
        self.param["pwd"] = pwd

        return self.send(self.data["login"])

    def recharge(self, member_id, amount, authorization):
        self.param["Authorization"] = authorization
        self.param["member_id"] = member_id
        self.param["amount"] = amount

        return self.send(self.data["recharge"])
