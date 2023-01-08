import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a,b",[(10,20),(10,5),(3,9)])
    def test_data1(self,a,b):
        print(a+b)

    @pytest.mark.parametrize(["a","b"],[(10,20),(10,5),(3,9)])
    def test_data2(self,a,b):
        print(a+b)

    @pytest.mark.parametrize(("a","b"),[(10,20),(10,5),(3,9)])
    def test_data3(self,a,b):
        print(a+b)

# 前面parametrize后面的变量，用元组、列表的区别：可以在第一个逗号前面加一个“."，可以看到元组、列表分别支持哪些方法
# 元组是不可变的，列表应用会更广泛
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml")))
    def test_data4(self,a,b):
        print(a-b)