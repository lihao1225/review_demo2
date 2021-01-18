from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo1:
    msg_ele = (MobileBy.XPATH, "//*[@resource-id = 'com.tencent.wework:id/gfj']//*[@text='消息']")
    work_ele = (MobileBy.XPATH,"//*[@resource-id = 'com.tencent.wework:id/gfj']//*[@text='工作台']")
    out_ele = (MobileBy.XPATH,"//*[@text='外出打卡']")
    punch_card_ele = (MobileBy.XPATH,"//*[contains(@text,'次外出')]")
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": True,
            "unicodeKeyboard": True,
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_demo1(self):
        self.driver.find_element(*self.msg_ele)
        self.driver.find_element(*self.work_ele).click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                         .scrollable(true).instance(0))\
                                         .scrollIntoView(new UiSelector()\
                                         .text("打卡").instance(0));').click()
        self.driver.update_settings({"waitForIdleTimeout":0})
        self.driver.find_element(*self.out_ele).click()
        self.driver.find_element(*self.punch_card_ele).click()
        WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功"in x.page_source)
