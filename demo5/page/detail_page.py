import os
import random

from demo5.common.handle_path import Data
from demo5.page.base_page import BasePage


class DetailPage(BasePage):

    def goto_detail_page(self):
        self.params["name"] = self.name()
        self.params["phone"] = self.phone()
        self.params["sex"] = "男"
        file_path = os.path.join(Data, "detail_page.yaml")
        self.parse_yaml(file_path, "detail_page")
        from demo5.page.manually_add_page import ManuallyAddPage
        return ManuallyAddPage(self.driver)

    def name(self):
        title_name = "lihao"
        name_value = str(random.randint(1000000, 9999999))
        name = title_name + name_value
        return name

    def phone(self):
        title_phone = "138"
        phone_num = str(random.randint(100000000, 999999999))
        phone = title_phone + phone_num[1:]
        return phone


