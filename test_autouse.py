import pytest
# 作用域: autouse="True"每次都会执行open方法
@pytest.fixture(autouse="True")
def open():
    print("打开浏览器")


def test_search1(open):
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

if __name__ == '__main__':
    pytest.main()