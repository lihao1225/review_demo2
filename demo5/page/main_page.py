import os

from demo5.common.handle_path import DirPath, Data
from demo5.page.base_page import BasePage
from demo5.page.address_page import AddressPage


class MainPage(BasePage):



    def goto_main(self):
        file_path = os.path.join(Data,"main.yaml")
        self.parse_yaml(file_path,"goto_msg")
        return AddressPage(self.driver)

