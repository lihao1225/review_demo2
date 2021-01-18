from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo2:

    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'android6',
            'browserName': 'Browser',
            'noReset': True,
            'unicodeKeyboard': True,
            "chromedriverExecutable": "/Users/huihuilina/Downloads/chromedriver-2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_demo(self):
        self.driver.get("http://www.baidu.com")
        sleep(10)
