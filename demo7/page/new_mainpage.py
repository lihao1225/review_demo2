from selenium.webdriver.common.by import By

from demo7.common.config import conf
from demo7.page.base_page import BasePage
from demo7.page.new_homework_page import NewHomeWorkPage


class  NewMainPage(BasePage):


    def add_class(self):
        nums = self.find_eles(By.XPATH,'//div[@class="qrcode"]//span')
        num = [i.get_attribute("textContent") for i in nums]
        if '课堂码:P69UVV' in num:
            self.paras_yaml("add_class.yaml","goto_class")
        else:
            self.params["class_num"] = conf.get("class","class_num")
            self.paras_yaml("add_class.yaml","add_class")
        return NewHomeWorkPage(self.driver)