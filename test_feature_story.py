import pytest
import allure
@allure.feature("登录模块")
class Test_Login():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录： 测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_success_a(self):
        print("这是登录： 测试用例，登录成功")
        pass

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert 1 == 1 # OK
            assert '1' == 1 # NOK
            print("登录失败 ")

        pass

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("这是登录： 测试用例，登录失败")
        pass

@allure.feature("搜索模块")
class Test_Search():
    @allure.story("搜索成功")
    def test_search_success(self):
        print("这是搜索： 测试用例，搜索成功")
        pass
if __name__ == '__main__':
    pytest.main()
