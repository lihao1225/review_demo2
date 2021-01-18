from demo5.page.base_page import BasePage
from demo5.page.main_page import MainPage


class TestDelete:

    def test_delete(self):
        delete = MainPage().goto_main().goto_search(). \
            search().personal_information().personal_information_two_page() \
            .edit_menbership().edit_menbership_two().goto_address().get_num()
        assert int(BasePage.after_num[0]) -1 == int(BasePage.end_num[0])