import os
from time import sleep

from selenium.webdriver.common.by import By

from demo7.common.handle_black import handle_black
from demo7.common.handle_path import DATA
from demo7.page.base_page import BasePage
from demo7.page.login_page import LoginPage


class HomePage(BasePage):
    base_url = "https://www.ketangpai.com/"

    @handle_black
    def goto_login(self):
        # file_path = os.path.join(DATA,"home_page.yaml")
        self.paras_yaml("home_page.yaml","goto_homepage")
        return LoginPage(self.driver)
