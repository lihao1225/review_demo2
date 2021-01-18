import yaml
from selenium.webdriver.android.webdriver import WebDriver

from appium import webdriver

from demo3.common.handle_black import handle_black


class BasePage:
    error_num = 0
    max_num = 3
    black_list = []

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            desired_caps = {
                'platformName': 'Android',
                'deviceName': 'emulator-5554',
                'appPackage': 'com.xueqiu.android',
                'appActivity': '.common.MainActivity',
                'noReset': True,
                'unicodeKeyboard': True
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
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



    def parse_yaml(self,file_path,func_name):
        """
        打开yaml进行读取文件
        :param file_path:
        :param func_name:
        :return:
        """
        with open(file_path,encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self,steps):
        """
        解析yaml文件
        :param steps:
        :return:
        """
        for step in steps:
            if 'click' == step["action"]:
                self.find(step["by"],step["locator"]).click()
            elif "send_key" == step["action"]:
                self.find(step["by"],step["locator"]).send_keys(step["text"])