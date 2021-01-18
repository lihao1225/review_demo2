from demo3.page.main_page import MainPage


class TestSearch():


    def test_search(self):
        search = MainPage().goto_search().search()