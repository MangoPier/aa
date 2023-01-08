import pytest
import allure

@allure.link("https://xueqiu.com/",name="雪球网站链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = 'https://docs.qameta.io/allure/#_pytest'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例的网站里面")
    pass

# 【暂未实现】终端运行时加上这一句，就代表bug链接到这个网址，这个括号传入的就是bug的ID值140：--allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
class TestClassWithTRIVIALseverity(object):
    def test_with_severity1(self):
        assert eval("3+4") == 7

    def test_with_severity2(self):
        assert eval("3+14") == 17

    @allure.severity(allure.severity_level.CRITICAL)
    def test_with_severity3(self):
        assert eval("3+4") != 17

@allure.severity(allure.severity_level.CRITICAL)
def test_with_severity():
    assert eval("3+4") != 17

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    # 这里写绝对路径会报错，原因待查
    # allure.attach.file("D:\Pythoncode\aa\Snipaste_2022-10-15_17-05-23.jpg",name="这是一张图片",attachment_type=allure.attachment_type.PNG)
    allure.attach.file("Snipaste_2022-10-15_17-05-23.jpg", name="这是一张图片",
                       attachment_type=allure.attachment_type.PNG)


if __name__=='__main__':
    pytest.main()

