from demo8.page.base_page import BasePage
from demo8.page.search_page import SearchPage


class MainPage(BasePage):

    def goto_search(self):
        self.paras_yaml("main_page.yaml","goto_search")
        return SearchPage(self.driver)
