import os
from time import sleep

from demo7.common.config import conf
from demo7.page.base_page import BasePage
from demo7.page.main_page import MainPage


class  LoginPage(BasePage):


    def login_page(self):
        self.params["phone"] = conf.get("login","phone")
        self.params["pwd"] = conf.get("login","pwd")
        self.paras_yaml("login_page.yaml","login_page")
        return MainPage(self.driver)