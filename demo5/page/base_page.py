import json

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from demo5.common.handle_black import handle_black


class BasePage:
    after_num=[]
    end_num =[]
    black_list = []
    error_num = 0
    max_num = 3
    params = {}

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            desired_caps = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True,
                "unicodeKeyboard": True
            }
            self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator):
        res = self.driver.find_elements(by, locator)
        return res

    def send_key(self, by, locator, text):
        self.driver.find_element(by, locator).send_keys(text)

    def scroll_ele(self, text):
        """
        滚动查找元素
        :param text:
        :return:
        """
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                                 .scrollable(true).instance(0))\
                                                 .scrollIntoView(new UiSelector()\
                                                 .text("{text}").instance(0));')

    def wait_for_ele(self, locator):
        """
        等待元素可见
        :param locator:
        :return:
        """
        result = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return result

    def wait_for_click(self, locator):
        """
        等待元素可被点击
        注意：在通过yaml文件打开locator时候需要用eval进行转换
        :param locator:
        :return:
        """
        result = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return result

    def get_toast(self):
        """
        获取toast
        :return:
        """
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast

    def parse_yaml(self, file_path, func_name):
        """
        解析yaml文件
        :param file_path:
        :param func_name:
        :return:
        """
        with open(file_path, encoding="utf-8") as f:
            data = yaml.load(f)
        # 替换文件中的内容
        if self.params is not None:
            self.replace_yaml(data[func_name])
        else:
            self.parse(steps=data[func_name])

    def parse(self, steps):
        """
        读取yaml文件
        :param steps:
        :return:
        """
        for step in steps:
            if 'click' == step["action"]:
                self.find(step["by"], step["locator"]).click()
            elif "send_key" == step["action"]:
                self.send_key(step["by"], step["locator"], step['text'])
            elif "scroll" == step["action"]:
                self.scroll_ele(step["text"]).click()
            elif "wait_for_vis" == step["action"]:
                self.wait_for_ele(eval(step["visible"]))
            elif "wait_for_click" == step["action"]:
                self.wait_for_click(eval(step["click"]))

    def replace_yaml(self, yaml_data):
        """
        替换yaml文件的变量
        :param yaml_data:
        :return:
        """
        raw_data = json.dumps(yaml_data)
        # print(self.params.items())
        # print(raw_data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        # print(data)
        # 替换后的yaml文件
        self.parse(data)
