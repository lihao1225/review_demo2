import os

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage
from demo5.page.edit_menbership_page import EditMenbershipPage


class PersonalInformationTwoPage(BasePage):


    def personal_information_two_page(self):
        file_path = os.path.join(Data, "personal_information_two.yaml")
        self.parse_yaml(file_path, "personal_information_two")
        return EditMenbershipPage(self.driver)
