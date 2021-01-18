import pytest


@pytest.fixture(scope="function")
def login():
    print("登录之前操作")
    yield
    print("登出操作")