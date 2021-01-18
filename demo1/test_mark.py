import pytest


class TestMark():
    @pytest.mark.login
    def test_login1(self):
        print("login1")

    @pytest.mark.login
    def test_login2(self):
        print("login2")

    @pytest.mark.search
    def test_search1(self):
        print("search1")

    @pytest.mark.search
    def test_search2(self):
        print("search2")
