from demo7.page.home_page import HomePage


class TestLogin():


    def test_login(self):
        main = HomePage().goto_login().login_page().goto_newpage()