from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDemo3:

    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.tencent.mm',
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            'noReset': True,
            'unicodeKeyboard': True,
            "chromedriverExecutable": "/Users/huihuilina/Downloads/chromedriver",
            "chromeOptions": {"androidProcess": "com.tencent.mm:appbrand0"},
            "adbPort": 5038,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_demo(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text = '通讯录']")
        sleep(2)
        rect = self.driver.get_window_size()
        width = rect["width"]
        height = rect["height"]
        self.driver.swipe(width*0.5,height*0.3,width*0.5,height*0.8,200)
        # action = TouchAction(self.driver)
        # x = width*0.5
        # y1 = height*0.3
        # y2 = height*0.8
        # action.press(x=x,y=y1).wait(200).move_to(x=x,y=y2).release().perform()
        self.driver.find_element(MobileBy.ID,"com.tencent.mm:id/lj").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text= '体验版']/../..//*[@text='泡泡抽盒机']").click()
        sleep(10)

        # self.driver.find_element(MobileBy.XPATH,"//*[@text='取消']")
        # self.driver.find_element(MobileBy.XPATH,"//*[@text = '搜索小程序']").send_keys("泡泡玛特")
