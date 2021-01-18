import pytest

from demo1.culcaltor import Calculator


@pytest.fixture(scope="module")
def per():
    cal = Calculator()
    print("计算开始")
    yield cal
    print("计算结束")
