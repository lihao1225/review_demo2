import os
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage
from demo5.page.personal_information_page import PersonalInformationPage


class SearchPage(BasePage):

    list_ele = (MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/dqe']/*")


    def search(self):
        file_path = os.path.join(Data, "search.yaml")
        self.parse_yaml(file_path, "search")
        name = self.finds(*self.list_ele)[-1].text
        self.scroll_ele(name).click()
        return PersonalInformationPage(self.driver)
    def goto_address(self):
        sleep(2)
        file_path = os.path.join(Data, "search.yaml")
        self.parse_yaml(file_path, "goto_address")
        from demo5.page.address_page import AddressPage
        return AddressPage(self.driver)
