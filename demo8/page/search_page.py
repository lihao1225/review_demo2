from demo8.page.base_page import BasePage


class SearchPage(BasePage):


    def search(self):
        self.paras_yaml("search_page.yaml","search")
        data = self.get_text(by='xpath',locator='//*[@resource-id="com.xueqiu.android:id/current_price"]')
        print(type(data))
        return data
