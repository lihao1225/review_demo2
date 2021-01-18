from time import sleep
import pyautogui as ui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestDemo4:



    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_demo4(self):
        self.driver.get("file:///Volumes/Untitled/PycharmProjects/webproject/web_05dom/iframe_demo.html")
        action = ActionChains(self.driver)
        e= self.driver.find_element_by_name("mfile")
        action.click(e).perform()
        """
        最好在python3.7版本安装,别的版本会有坑
        pip install pillow==6.2.2
        pip install pyautogui
        #处理中文的路径
        pip install pyperclip----用于处理剪切板的第三方库
        """
        #
        # #发送数据
        import pyautogui as ui
        sleep(2)
        ui.write(r"/Users/huihuilina/Desktop/shuju.txt")
        sleep(2)
        ui.press("enter",presses=3)
        sleep(4)
        #处理中文路径文件
        # import pyperclip
        # pyperclip.copy("文件路径")
        # sleep(2)
        # ui.hotkey('ctrl','v')
        # ui.press("enter",presses=2)
        # sleep(4)

