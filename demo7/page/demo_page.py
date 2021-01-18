import os
from time import sleep

from selenium.webdriver.common.by import By

from demo7.common.handle_path import DATA
from demo7.page.base_page import BasePage


class DemoPage(BasePage):
    # base_url = "http://sahitest.com/demo/clicks.htm"
    # base_url = "http://sahitest.com/demo/dragDropMooTools.htm"
    # base_url = "http://sahitest.com/demo/label.htm"
    # base_url = "http://www.baidu.com"
    # base_url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu"
    def demo1(self):
        "鼠标点击"
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo1")

    def demo2(self):
        "鼠标拖拽"
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo2")
    def demo3(self):
        """
        键盘操作
        :return:
        """
        "鼠标拖拽"
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo3")
        sleep(3)
    def demo4(self):
        """
        复制粘贴
        :return:
        """
        self.params["text"] = '1234'
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo4")
        sleep(3)

    def demo5(self):
        """
        屏幕滑动
        :return:
        """
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo5")

    def demo6(self):
        """
        窗口跳转
        :return:
        """
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo6")
        return self.get_url()

    def demo7(self):
        file_path = os.path.join(DATA, "demo.yaml")
        self.paras_yaml(file_path, "demo7")

    def demo8(self):
        self.get_cookie()
        # self.add_cookie()

    def goto_address(self):
        self.add_cookie()
        file_path = os.path.join(DATA, "weixin.yaml")
        #上传文件名称data
        self.paras_yaml(file_path, "homepage")
        return self.get_ele_text('xpath','//div[text()="11.xls"]')


