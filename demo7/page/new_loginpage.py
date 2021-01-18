from demo7.common.config import conf
from demo7.page.base_page import BasePage
from demo7.page.new_mainpage import NewMainPage


class NewLoginPage(BasePage):


    def new_login_page(self):
        self.params["phone"] = conf.get("login","phone")
        self.paras_yaml("new_loginpage.yaml","new_loginpage")
        return NewMainPage(self.driver)