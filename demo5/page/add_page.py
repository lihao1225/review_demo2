import os

from demo5.common.handle_path import DirPath, Data
from demo5.page.base_page import BasePage
from demo5.page.manually_add_page import ManuallyAddPage


class AddPage(BasePage):

    def goto_add(self):
        file_path = os.path.join(Data, "add.yaml")
        self.parse_yaml(file_path, "add")
        return ManuallyAddPage(self.driver)
