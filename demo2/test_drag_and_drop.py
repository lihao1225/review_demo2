from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException



class TestDragAndDrop:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele1 = self.driver.find_element(By.XPATH, '//div[text()="Item 1"]')
        drop_ele2 = self.driver.find_element(By.XPATH, '//div[text()="Item 2"]')
        drop_ele3 = self.driver.find_element(By.XPATH, '//div[text()="Item 3"]')
        drop_ele4 = self.driver.find_element(By.XPATH, '//div[text()="Item 4"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele1).pause(1)
        action.drag_and_drop(drag_ele, drop_ele2).pause(1)
        action.drag_and_drop(drag_ele, drop_ele3).pause(1)
        action.drag_and_drop(drag_ele, drop_ele4).perform()
        sleep(3)
    # @pytest.mark.skip
    def test_send_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        input1 = self.driver.find_elements(By.XPATH,"//input[@type = 'textbox']")[0]
        input2 = self.driver.find_elements(By.XPATH,"//input[@type = 'textbox']")[1]

        # input1.send_keys("123456")
        # input1.send_keys(Keys.BACK_SPACE)

        action = ActionChains(self.driver)
        input1.click()
        # action.send_keys("123445").perform()
        sleep(1)
        # action.send_keys(Keys.BACK_SPACE)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
        input2.click()
        action.key_down(Keys.CONTROL,input2).send_keys("v").key_up(Keys.CONTROL).perform()
        sleep(2)

    @pytest.mark.skip
    def test_touch_action(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        search_ele = self.driver.find_element_by_id("su")
        action.tap(search_ele).perform()
        action.scroll_from_element(ele,0,10000)
        last_page=self.driver.find_element(By.XPATH,"//div[@id='page']/div/a[contains(text(),'下一页')]")
        action.perform()
        self.driver.find_elements(By.XPATH,"//div[@id = 'page']/div/a")[-1].click()
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@id='page']/div/a[contains(text(),'下一页')]")))
        # action.tap(last_page)
    @pytest.mark.skip
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.XPATH,"//div[@id = 'u1']/a[text()='登录']").click()
        sleep(2)
        register=(By.XPATH,"//a[text()='立即注册']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(register))
        self.driver.find_element(By.XPATH,"//a[text()='立即注册']").click()
        window_handle = self.driver.window_handles
        self.driver.switch_to.window(window_handle[-1])
        user_ele = (By.ID,"TANGRAM__PSP_4__userName")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(user_ele))
        self.driver.find_element(*user_ele).send_keys("1234")
    @pytest.mark.skip
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element(By.ID,"draggable")
        drop = self.driver.find_element(By.ID,"droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(1)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,"submitBTN").click()
    @pytest.mark.skip
    def test_execute_script(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys("selenium")
        self.driver.execute_script("document.getElementById('su').click()")
        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        self.driver.find_element(By.CSS_SELECTOR,'#page > div > a.n').click()

    @pytest.mark.skip
    def test_execute_script1(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(1)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-28'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))





