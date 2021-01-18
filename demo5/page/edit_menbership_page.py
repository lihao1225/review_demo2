import os

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage
from demo5.page.edit_menbership_two_page import EditMenbershipTwoPage


class EditMenbershipPage(BasePage):


    def edit_menbership(self):
        file_path = os.path.join(Data, "edit_menbership.yaml")
        self.parse_yaml(file_path, "edit_menbership")
        return EditMenbershipTwoPage(self.driver)