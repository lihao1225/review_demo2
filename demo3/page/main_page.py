import yaml
import os

from demo3.common.handle_path import DATA
from demo3.page.base_page import BasePage
from demo3.page.search_page import SearchPage


class MainPage(BasePage):

    def goto_search(self):
        yaml_path = os.path.join(DATA, "main.yaml")
        self.parse_yaml(yaml_path, "goto_search")
        return SearchPage(self.driver)