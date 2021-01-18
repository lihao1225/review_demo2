from demo7.page.base_page import BasePage
from demo7.page.new_homepage import NewHomePage


class MainPage(BasePage):


    def goto_newpage(self):
        self.paras_yaml("main.yaml","main_page")
        return NewHomePage(self.driver)