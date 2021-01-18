from time import sleep

from demo3.common.handle_path import DATA
from demo3.page.base_page import BasePage
import os

class SearchPage(BasePage):

    def search(self):
        sleep(1)
        yaml_path = os.path.join(DATA, "search.yaml")
        self.parse_yaml(yaml_path, "search1")
