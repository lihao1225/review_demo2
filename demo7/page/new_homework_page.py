from demo7.page.base_page import BasePage


class NewHomeWorkPage(BasePage):


    def goto_homework_tab(self):
        self.paras_yaml("homework_page.yaml","goto_homework_tab")