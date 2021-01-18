from demo7.page.demo_page import DemoPage


class TestDemo():


    def test_demo(self):

        # main = DemoPage().demo1()
        # demo2 = DemoPage().demo2()
        # demo3 = DemoPage().demo6()
        # assert "http://news.baidu.com/" == demo3
        # demo7 = DemoPage().demo8()
        demo_weixin = DemoPage().goto_address()
        assert "11.xls" == demo_weixin