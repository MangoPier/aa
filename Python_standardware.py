#--1、 Python 标准库-------------------------------------------------------------------------------------
# os模块 ---------------------------------------------------------------------------------------
import os
# os.mkdir("testdir")
import sys
import time

import allure
'''
print(os.listdir("./"))
# os.removedirs("testdir")
print(os.getcwd())  # 返回当前目录

# os.path.exists("b") # 判断是否存在
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt","w")
    f.write("hello,os using")
    f.close()

# time模块 ---------------------------------------------------------------------------------------
import time
print(time.asctime()) # Sat Oct 15 11:01:06 2022
print(time.time()) # 1665802866.9844303，从纪元到现在的秒数
print(time.localtime())
# time.struct_time(tm_year=2022, tm_mon=10, tm_mday=15, tm_hour=11, tm_min=1, tm_sec=6, tm_wday=5, tm_yday=288, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 2022-10-15 11:04:17

import locale
locale.setlocale(locale.LC_CTYPE,'chinese')
# 解决下一步可能出现的问题：UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: encoding error
print(time.strftime("%Y年%m月%d日 %H:%M:%S",time.localtime()))
# 2022年10月15日 11:08:16

# 获取两天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
# 60秒60分钟24小时2天
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(two_day_before)))
# 2022-10-13 11:12:59

# urllib库
import urllib
# import urllib.request
# response: object= urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.read())
# print(response.headers)

import math
print(math.ceil(90.111))
# 91
print(math.floor(90.1111))
# 90
print(math.sqrt(9))
# 3.0 返回浮点数
'''

# 2、线程 -------------------------------------------------------------------------------------

'''
import os
import logging
from time import sleep
# from pip._internal import main
from pytest import main
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://oa.vastdata.com.cn/seeyon/main.do")
# assert "vastdata" in driver.title
elem = driver.find_element(By.NAME,"login_username")
elem.clear()
elem.send_keys("zhaofj")
elem.send_keys(Keys.RETURN)
# elemnpw = driver.find_element_by_name("login_password") # selenium版本升级，不支持该功能
elemnpw = driver.find_element(By.NAME,"login_password")
# elemnpw.send_keys("***")
elemnpw.click()
assert "No results found." not in driver.page_source
# driver.close()
'''

import logging
import threading
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

loops = [2,4]
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop,nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at "+ ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ == "__main__":
    main()

# 原语——一般是指由若干条指令组成的程序段，用来实现某个特定功能，在执行过程中不可被中断。
# # 锁，解决了数据的互斥访问
# # 信号量

# 10、allure -------------------------------------------------------------------------------------
# 轻量级、灵活、支持多语言的测试报告工具
'''
import pytest
# 官网用例一
'''

def test_success():
    assert True

def test_failure():
    assert False

def test_skip():
    pytest.skip('for a reason!')

def test_broken():
    raise Exception('oops')

# 用例二
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "http://oa.vastdata.com.cn/seeyon/main.do"

driver.get(url)

'''

# @allure.story("用户名缺失")
# 用例三
'''

import allure
@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
    print("这是一个加了链接的测试")
    pass

TEST_CASE_OALINK = "http://oa.vastdata.com.cn/seeyon/main.do"
@allure.testcase(TEST_CASE_OALINK,"登录用例")
def test_with_testcase_link():
    print("这是一条测试用例的链接")
    pass

# 给测试用例的bug一个链接。未实践成功【 pytest .\Python_standardware.py --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{} --alluredir=./result/9】
# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_severity():
    pass

def test_with_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)
    pass

def test_with_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_attac_photo():
    allure.attach.file("./Snipaste_2022-10-15_17-05-23.jpg",attachment_type=allure.attachment_type.JPG) # 要写相对路径。如果不用file方法，那么测试报告里面无法打开照片

'''
# 用例4
'''

import pytest
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.baidu.com")

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element(By.ID,"kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element(By.ID,"su").click()
        time.sleep(2)
    # 以下方法只能保存最后一个关键字的搜索截图
    with allure.step("保存图片"):
        driver.save_screenshot('./result/b.png')
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()

if __name__ == '__main__':
    pytest.main(['-s', '-vv', 'Python_standardware.py','--alluredir', './report/xml'])
'''

# 命令行执行：pytest .\Python_standardware.py  --alluredir=./result/9
# pycharm执行方法：
# 右键有修改运行配置，其他实参：--alluredir=./reslut/0 --allure-severities trivial














