from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver


class TestToast:

    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": 'emulator-5554',
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.view.PopupMenu1",
            "noReset": True,
            'unicodeKeyboard': True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text = 'Make a Popup!']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text = 'Search']").click()
        print(self.driver.page_source)
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text
        assert 'Clicked popup menu item Search' == toast
