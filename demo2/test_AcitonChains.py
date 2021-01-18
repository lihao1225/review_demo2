from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChains():


    def setup(self):
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        pass

    def test_action_chains(self):
        self.driver.get("http://www.baidu.com")
        action = ActionChains(self.driver)
        ele1 = self.driver.find_element_by_id("s-usersetting-top")
        action.move_to_element(ele1).perform()
        sleep(2)

