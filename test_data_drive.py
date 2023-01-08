import pytest
import yaml

class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print(env)
            # 如果yaml是列表嵌套字典，那么print(env)打印出来的是：{'test': '127.0.0.1'}
            # 如果yaml是字典，那么print(env)打印出来的是：test。因为字典格式，传入参数env，会打印的是key，而不是value
            print("测试环境的IP是: ",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            # print("开发环境的IP是：",env["dev"])

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml",encoding='utf-8')))
# 如果yaml文件内容是列表格式，那么打印出来的结果是：['test:127.0.0.1']
# 如果yaml文件内容是字典格式，那么打印出来的结果是：{'test': '127.0.0.1'}


