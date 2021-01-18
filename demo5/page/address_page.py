import os
import re

from appium.webdriver.common.mobileby import MobileBy

from demo5.common.handle_path import DirPath, Data
from demo5.page.add_page import AddPage
from demo5.page.base_page import BasePage
from demo5.page.search_page import SearchPage


class AddressPage(BasePage):

    def goto_address(self):
        """
        点击进入通讯录
        :return:
        """
        file_path = os.path.join(Data, "address.yaml")
        self.parse_yaml(file_path, "address")
        return AddPage(self.driver)

    def goto_search(self):
        """
        点击进入搜索页
        :return:
        """
        file_path = os.path.join(Data, "address.yaml")
        self.parse_yaml(file_path, "address")
        self.scroll_ele("添加成员")
        self.wait_for_ele((MobileBy.XPATH,'//*[contains(@text,"共")]'))
        after_text =self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"共")]').text
        after_num = re.findall('(?<=共).*?(?=人)',after_text)[0]
        self.after_num.append(after_num)
        print(self.after_num[0])
        self.parse_yaml(file_path, "goto_search")
        return SearchPage(self.driver)

    def get_num(self):
        self.scroll_ele("添加成员")
        self.wait_for_ele((MobileBy.XPATH, '//*[contains(@text,"共")]'))
        end_text = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"共")]').text
        end_num = re.findall('(?<=共).*?(?=人)', end_text)[0]
        self.end_num.append(end_num)
