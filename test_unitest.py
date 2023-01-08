import os.path
import time
import unittest
from Lib.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None: # setup、teardown方法自动调用，这里是复用方法，还增加了print。每个case执行之前都会跑一遍setup、teardown
        print("setup")

    def tearDown(self) -> None: # 比如执行之前需要考虑数据、资源、登录，那么就可以用setup、teardown
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(1,1,"判断相等")
        self.assertIn('h','this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(2,2,"判断相等")

    @unittest.skip # 这里会跳过以下用例
    # @unittest.skip(1+1==2,"满足这个条件时，跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3,3,"判断相等")

class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_  case0")
    def test_demo1_case1(self):
        print("test_demo1_  case1")

class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo2_  case0")
    def test_demo2_case1(self):
        print("test_demo2_  case1")
"""
# 执行顺序
setup class
setup
testcase01
teardown
setup
testcase02
teardown
teardown class
"""


# if __name__ == '__main__':
# 执行方法一
    # unittest.main()
# 执行方法二:加入容器中执行
#     suite = unittest.TestSuite()
#     suite.addTest(demo("test_case01"))
#     suite.addTest(demo1("test_demo1_case0"))
#     unittest.TextTestRunner().run(suite)
# 执行方法三:可以同时测试多个类
    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite,suite1])
    # unittest.TextTestRunner().run(suiteall)
# 执行方法四:匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
#     discover = unittest.defaultTestLoader.discover("./",'test*.py')
#     unittest.TextTestRunner().run(discover)
#     report_title = 'example 用例执行报告'
#     desc = '用于展示修改样式后的HTMLTestRunner'
#     report_file = './ExampleReport.html'
#     testsuite = unittest.TestSuite()
#     testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo))
#     testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo2))

#     with open(report_file,'wb') as report:
#         runner = HTMLTestRunner(stream = report,title = report_title,description = desc)
#         runner.run(testsuite)

# 定义存放测试报告的路径和文件名
# 我定义的路径是：当前路径+存放报告的专有目录Report+文件名(文件名是当前时间+report.html)
# filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),"pyresult.html")
current_dirc = os.path.dirname(os.path.realpath(__file__))
report_dirc = "./report"
now = time.strftime("%Y%m%d-%H%M%S")
report_name = current_dirc + report_dirc + "\\" + now + "_report.html"
fp = open(report_name,"wb")
'''
# 这三步打印没有显示出来，待查
print(current_dirc)
print(report_name)
print("___________________________________hhhh__________________________________")
'''

runner = HTMLTestRunner(stream=fp,title=u'这是一个测试报告的标题哈哈哈哈哈哈',description="单元测试的测试用例哈哈哈哈哈")
# 构建测试集cd
test_suit = unittest.TestSuite()
# 在这个套件中添加测试用例，可以通过类名、模块名、文件名等加载。以下三种方法都可以
# test_suit.addTests([demo("test_case01"),demo2("test_demo2_case1")])
# test_suit.addTests(map(demo,["test_case01","test_case02"])) # map 代表映射
test_suit.addTests(unittest.TestLoader().loadTestsFromTestCase(demo2))
runner.run(test_suit)
print("~"*30)
fp.close()
