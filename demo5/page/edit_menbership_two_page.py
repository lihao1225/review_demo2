import os

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage


class EditMenbershipTwoPage(BasePage):


    def edit_menbership_two(self):
        file_path = os.path.join(Data, "edit_menbership_two.yaml")
        self.parse_yaml(file_path, "edit_menbership_two")
        from demo5.page.address_page import AddressPage
        from demo5.page.search_page import SearchPage
        return SearchPage(self.driver)