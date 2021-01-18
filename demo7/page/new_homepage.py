from demo7.page.base_page import BasePage
from demo7.page.new_loginpage import NewLoginPage


class NewHomePage(BasePage):


    def goto_login(self):
        self.paras_yaml("new_homepage.yaml","goto_login")
        return NewLoginPage(self.driver)