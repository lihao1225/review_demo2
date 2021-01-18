from demo5.page.main_page import MainPage


class TestAdd():


    def test_add(self):
        add = MainPage().goto_main().goto_address().goto_add().goto_manually_add_page().goto_detail_page().get_toast1()
        assert "添加成功" == add