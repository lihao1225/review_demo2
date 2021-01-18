import json
import os
import shelve
import time
from time import sleep

import allure
import yaml
from selenium import webdriver
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from demo7.common.handle_black import handle_black
from demo7.common.handle_log import log
from demo7.common.handle_path import DATA


class BasePage():
    base_url = ''
    error_num = 0
    max_num = 3
    black_list = [(By.XPATH, "//div[@id = 'layui-layer1']/span/a")]
    params = {}

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            # option = webdriver.ChromeOptions()
            # option.add_experimental_option("w3c",False)
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def save_screenshot(self):
        """
        通过allure进行电脑截图
        :return:
        """
        # 截屏操作
        self.driver.save_screenshot("tmp.png")
        with open("tmp.png", "rb") as f:
            content = f.read()
        # 通过allure进行电脑截屏保存到allure报告中
        allure.attach(content, attachment_type=allure.attachment_type.PNG)

    @handle_black
    def find_ele(self, by, locator):
        """
        查找元素方法
        :return:
        """
        if locator is None:
            res = self.driver.find_element(*by)
        else:
            res = self.driver.find_element(by, locator)
        return res

    def find_eles(self, by, locator):
        """
        查找多个元素
        :return:
        """
        res = self.driver.find_elements(by, locator)
        return res

    def send_key(self, by, locator, text):
        """
        输入信息
        :param by:
        :param locator:
        :param text:
        :return:
        """
        try:
            result = self.find_ele(by, locator).send_keys(text)
            return result
        except Exception as e:
            self.save_screenshot()
            raise e

    def wait_for_element(self, locator):
        """
        显示等待元素可以被查找
        :param locator:
        :return:
        """
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return ele

    def presence_of_element_located(self, locator):
        """
        等待元素被加载
        :param locator:
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
            return ele
        except Exception as e:
            self.save_screenshot()
            raise e

    def element_to_be_clickable(self, locator):
        """
        等待元素被点击
        :param locator:
        :return:
        """

        try:
            ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
            return ele
        except Exception as e:
            self.save_screenshot()
            raise e

    def get_ele_text(self, by, locator):
        """

        :param by:
        :param locator:
        :return:
        """
        res = self.find_ele(by, locator).get_attribute('textContent')
        return res

    def get_cookie(self):
        """
        获取cookie
        :return:
        """
        sleep(15)
        cookie = self.driver.get_cookies()
        db = shelve.open("cookies")
        db["cookie"] = cookie
        db.close()

    def add_cookie(self):
        """
        添加cookie
        :return:
        """
        db = shelve.open("cookies")
        cookies = db["cookie"]
        self.driver.get(self.base_url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def keyboard(self, by, locator):
        ele = self.find_ele(by, locator)
        ele.send_keys(Keys.SPACE)
        ele.send_keys("tom")
        ele.send_keys(Keys.BACKSPACE)

    def scroll_element(self, height):
        """
        滑动屏幕
        0:代表的是x坐标也就是横坐标
        10000：代表的是y轴为纵坐标
        :param ele: 起始位置元素
        :return:
        """
        # action = TouchActions(self.driver)
        # action.scroll_from_element(ele,0,10000).perform()
        self.driver.execute_script(f'document.documentElement.scrollTop = {height}')

    def scrollIntoView(self, by, locator):
        """
        滚动查找
        :param by:
        :param locator:
        :return:
        """

        ele = self.find_ele(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def execute_script(self, js):
        """
        通过js驱动浏览器
        :param js: js语句
        :return:
        """
        res = self.driver.execute_script(js)
        return res

    def switch_window(self):
        """
        窗口跳转
        :return:
        """

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])

    def switch_frame(self, value):
        """
        跳转frame
        :param value: 可以是frame的ID，name ,webelement
        :return:
        """

        self.driver.switch_to.frame(value)

    def tap_frame(self):
        """
        切换到默认的frame
        :return:
        """
        self.driver.switch_to.default_content()

    def parent_frame(self):
        """
        切换到父类的frame
        :return:
        """
        self.driver.switch_to.parent_frame()

    def switch_alert_accept(self):
        """
        弹框确定按钮
        :return:
        """
        self.driver.switch_to.alert.accept()

    def switch_alert_dismiss(self):
        """
        弹框取消按钮
        :return:
        """
        self.driver.switch_to.alert.dismiss()

    def switch_alert_text(self):
        """
        获取弹框文案
        :return:
        """

        self.driver.switch_to.alert.text()

    def switch_alert_sendkey(self, text):
        """
        弹框输入文案
        :param text:
        :return:
        """
        self.driver.switch_to.alert.send_keys(text)

    def get_url(self):
        """
        获取当前页面URL
        :return:
        """
        url = self.driver.current_url
        return url

    def copy_and_paste(self, ele1, ele2, text):
        """

        :param ele1: 复制的元素
        :param ele2: 粘贴的元素
        :return:
        """
        action = ActionChains(self.driver)
        ele1.click()
        action.send_keys(text).perform()
        sleep(1)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
        ele2.click()
        action.key_down(Keys.CONTROL, ele2).send_keys("v").key_up(Keys.CONTROL)
        action.perform()
        sleep(3)

    def right_click(self, by, locator):
        """
        右击鼠标
        :param by:
        :param locator:
        :return:
        """
        ele = self.find_ele(by, locator)
        action = ActionChains(self.driver)
        result = action.context_click(ele).perform()
        return result

    def double_click(self, by, locator):
        """
        双击鼠标
        :param by:
        :param locator:
        :return:
        """

        ele = self.find_ele(by, locator)
        action = ActionChains(self.driver)
        result = action.double_click(ele).perform()
        return result

    def move_to_element(self, by, locator):
        """
        鼠标移动到某个元素
        :param by:
        :param locator:
        :return:
        """
        ele = self.find_ele(by, locator)
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()

    def sleep(self, time):
        sleep(time)

    def drag_and_drop(self, drag_ele, drop_ele):
        """
        拖拽元素
        :param drag_ele:
        :param drop_ele:
        :return:
        """
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele).perform()

    def paras_yaml(self, file_name, func_name):
        """

        :param file_path: yaml文件的路径
        :param func_name: yaml文件的模块
        :return:
        """
        file_path = os.path.join(DATA, f"{file_name}")
        with open(file_path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.replace_yaml(data[func_name])

    def replace_yaml(self, data):
        """
        替换yaml文件中的参数
        :param data:
        :return:
        """
        raw_data = json.dumps(data)

        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        self.paras(data)

    def paras(self, steps):
        """

        :param steps:
        :return:
        """
        for step in steps:
            if step["action"] == "click":
                self.find_ele(step["by"], step["locator"]).click()
            elif step["action"] == "find":
                self.find_ele(step["by"], step["locator"])
            elif step["action"] == "send_key":
                self.find_ele(step["by"], step["locator"]).send_keys(step["text"])
            elif step["action"] == "right_click":
                self.right_click(step["by"], step["locator"])
            elif step["action"] == "double_click":
                self.double_click(step["by"], step["locator"])
            elif step["action"] == "drag_and_drop":
                drag_ele = self.find_ele(step["by"], step["locator"])
                drop_ele = self.find_ele(step["by1"], step["locator1"])
                self.drag_and_drop(drag_ele, drop_ele)
            elif step["action"] == "keyboard":
                self.keyboard(step["by"], step["locator"])
            elif step["action"] == "copy_and_paste":
                ele1 = self.find_ele(step["by"], step["locator"])
                ele2 = self.find_ele(step["by1"], step["locator1"])
                self.copy_and_paste(ele1, ele2, step["text"])
            elif step["action"] == "scroll_element":
                # ele = self.find_ele(step["by"],step["locator"])
                # self.scroll_element(ele)
                self.scroll_element(step["height"])
            elif step["action"] == "execute_script":
                self.execute_script(step["js"])
            elif step["action"] == "switch_window":
                self.switch_window()
            elif step["action"] == "frame":
                self.switch_frame(step["frame_id"])
            elif step["action"] == "switch_alert_accept":
                self.switch_alert_accept()
            elif step["action"] == "tap_frame":
                self.tap_frame()
            elif step["action"] == "wait_for_element":
                self.wait_for_element(eval(step["locator"]))
            elif step["action"] == "sleep":
                self.sleep(step["time"])
            elif step["action"] == "presence_of_element_located":
                self.presence_of_element_located(eval(step["locator"]))
            elif step["action"] == "element_to_be_clickable":
                self.element_to_be_clickable(eval(step["locator"]))
            elif step["action"] == "move_to_element":
                self.move_to_element(step["by"], step["locator"])
            elif step["action"] =="scrollIntoView":
                self.scrollIntoView(step["by"],step["locator"])


    # def _find_elem_by_xpath(self, elem_xpath, time_out=timeout, raise_exception=True):
    #     start = time.time()
    #     elem = None
    #     while time.time() - start < time_out and elem is None:
    #         time.sleep(poll)
    #         try:
    #             elem = self.driver.find_element_by_xpath(elem_xpath)
    #         except Exception:
    #             print('by pass the element not found')
    #
    #     if elem is None and raise_exception:
    #         raise LookupError(f'The element which xpath is {elem_xpath} could not be found')
    #
    #     return elem
