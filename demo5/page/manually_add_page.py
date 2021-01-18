import os

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage
from demo5.page.detail_page import DetailPage


class ManuallyAddPage(BasePage):

    def goto_manually_add_page(self):
        file_path = os.path.join(Data, "manually_add.yaml")
        self.parse_yaml(file_path, "manually_add")
        return DetailPage(self.driver)

    def get_toast1(self):
        res = self.get_toast()
        return res
