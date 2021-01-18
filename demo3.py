from time import sleep
import shelve
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo3:

    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        pass
    @pytest.mark.skip
    def test_demo_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #获取cookies
        sleep(15)
        cookies = self.driver.get_cookies()
        db = shelve.open("cookies")
        db["cookie"] = cookies
        db.close()
        sleep(2)
    def test_add_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies")
        cookies = db["cookie"]
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
