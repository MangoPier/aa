import pytest
import sys
# 参数化，前两个变量，后面是对应的数据：
# 3+5->test_input   8->expect
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
def test_eval(test_input,expected):
#     eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected

# 参数组合。可以传入多组参数
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,11])
def test_foo(x,y):
    print(f"测试数据组合x:{x},y:{y}")
#     这里有2*3=6条测试用例

# 方法名作为参数
# 应用场景举例：用户名如果有多种文字、符号，可以通过这个方法传参
test_user_data = ['Tom','Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    # 这里是接收并传入的参数
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user

# 两种忽略测试用例的方法：一个是有条件地忽略，一个是直接忽略
# @pytest.mark.skipif(sys.platform == "darwin",reason="不在macos上面执行")
# @pytest.mark.skip("此次测试不执行登录")
# 不论是否通过，标记测试用例为通过。比如说有这种场景：这次测试明确不会通过，就先标记为XPASS
@pytest.mark.xfail
# 传参
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
# 如果没有传参，会报错。没有indirect=True，会跳过login_r这个方法调用
# indirect=True，可以把传过来的参数当函数来执行
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""
    # raise NameError # 配合前面的xfail，在测试报告体现xfail


if __name__ == '__main__':
    pytest.main('-v')