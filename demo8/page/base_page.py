import json
import os

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from demo8.common.handle_black import handle_black
from demo8.common.handle_path import DATA


class BasePage():
    error_num = 0
    max_num = 3
    black_list = []
    params = {}

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            desired_caps = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True

            }
            self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver = driver

    def restart(self):
        """
        重启app
        :return:
        """
        self.driver.close_app()
        self.driver.launch_app()

    def stop_app(self):
        """
        关闭app
        :return:
        """
        self.driver.quit()

    @handle_black
    def find(self, by, locator):
        """
        查找元素
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result
    def get_text(self,by,locator):
        """
        获取元素文本
        :param by:
        :param locator:
        :return:
        """
        result = self.find(by,locator).text
        return result

    def paras_yaml(self, file_name, func_name):
        """
        解析yaml文件
        :param file_path: yaml文件路径
        :param func_name: yaml文件列表名
        :return:
        """

        file_path = os.path.join(DATA, f"{file_name}")
        with open(file_path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.replace_yaml(data[func_name])

    def replace_yaml(self, data):
        """
        替换yaml文件的变量数据
        :param data:
        :return:
        """

        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)

        self.paras(data)

    def paras(self, steps):
        """
        测试步骤参数化
        :param steps:
        :return:
        """
        for step in steps:
            if step["action"] == "click":
                self.find(step["by"], step["locator"]).click()
            elif step["action"] == "send_key":
                self.find(step["by"], step["locator"]).send_keys(step["text"])
            elif step["action"] == "get_text":
                self.get_text(step["by"], step["locator"])
