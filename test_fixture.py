import pytest
# 基本用法
# @pytest.fixture()
# def login():
#     print("这是一个登录方法")
# 改进方法：把上面fixture方法放在conftest.py文件里面

def test_case1(login): # 这里在测试方法传入参数login，代表先进行登录，再执行测试用例
    print("test_case1,需要登录")

def test_case2():
    print("test_case2,不需要登录")

def test_case3(login):
    print("test_case3,需要登录")

if __name__ == '__main__':
    pytest.main()
