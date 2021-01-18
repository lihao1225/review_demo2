from demo8.page.main_page import MainPage


class TestDemo():



    def test_demo1(self):
        main = MainPage().goto_search().search()
        print(main)