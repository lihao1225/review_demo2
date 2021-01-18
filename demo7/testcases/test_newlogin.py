from demo7.page.home_page import HomePage


class TestNewLogin():


    def test_new_login(self):

        main=HomePage().goto_login().login_page().goto_newpage()\
            .goto_login().new_login_page().add_class()\
            .goto_homework_tab()