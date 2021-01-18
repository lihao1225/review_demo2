import pytest
import requests
from requests.auth import HTTPBasicAuth


# @pytest.fixture(scope="module")
# def login():
#     print("这是个登录方法")
#     yield
#
#     print("这是登出方法")


# @pytest.fixture()
# def operate():
#     print("登录后操作")

@pytest.mark.usefixtures("login")
def test_case1():
    print("test_case")


def test_case2():
    print("test_case2")


def test_case3():
    print("test_case3")






