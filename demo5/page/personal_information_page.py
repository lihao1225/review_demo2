import os

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage
from demo5.page.personal_information_two_page import PersonalInformationTwoPage


class PersonalInformationPage(BasePage):


    def personal_information(self):
        file_path = os.path.join(Data, "personal_information.yaml")
        self.parse_yaml(file_path, "personal_information")
        return PersonalInformationTwoPage(self.driver)