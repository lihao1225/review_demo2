import os

import allure
import jsonpath
import yaml

from demo6.api.register_api import RegisterApi
import pytest

from demo6.common.handle_log import log
from demo6.common.handle_path import Data
from demo6.testcase.test_base import TestBase


def data():
    file_path = os.path.join(Data, "data.yaml")
    with open(file_path, encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

@allure.feature("充值接口")
class TestRegister(TestBase):

    @pytest.mark.parametrize("mobile,pwd",data()["register"] )
    def test_register(self, mobile, pwd):
        main = RegisterApi().register(mobile=mobile, pwd=pwd)
        print(main)
    # @pytest.mark.login()
    # def test_login(self):
    #     login = RegisterApi().login(mobile="13812345670", pwd="12345678")
    #     print(login)
    #     assert login["code"] == 0
    #     assert login["msg"] == "OK"
    #     return login
    @allure.story("充值成功")
    def test_recharge(self):
        # login = RegisterApi().login(mobile="13812345670", pwd="12345678")
        with allure.step("充值成功"):
            token_type = jsonpath.jsonpath(self.login, "$..token_type")[0]
            token = jsonpath.jsonpath(self.login, "$..token")[0]
            member_id = str(jsonpath.jsonpath(self.login, "$..id")[0])
            authorization = token_type + " " + token
            recharge = RegisterApi().recharge(member_id=member_id, amount='1000', authorization=authorization)
            try:
                assert recharge["code"] == 0
                assert recharge["msg"] == 'OK'
            except Exception as e:
                log.error(f"测试用例{RegisterApi().data['recharge']['url']}未通过")
                log.exception(e)
                raise e
            else:
                log.info(f"测试用例{RegisterApi().data['recharge']['url']}通过")
