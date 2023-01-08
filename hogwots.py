# 列表
'''
print("-----------------list-------------")
list_hog = [1,2,3]
list_hog.append(0)
list_hog.insert(1,0)
print(list_hog)
list_hog.remove(0)
print(list_hog)
y = list_hog.pop(1)
print(y)
list_hog.append(-1)
list_hog.sort()
print(list_hog)
list_hog.sort(reverse=True) # 倒序
print(list_hog)
list_hog.reverse()
print(list_hog)
list_hog.clear()
print(list_hog)

list_square = []
for i in range(4):
    list_square.append(i**2)

print(list_square) # [0, 1, 4, 9]
# 列表推导式
list_square2 = [i **2 for i in range(1,4)]

print(list_square2)

list_square3 = []
for i in range(1,4):
    if i!=1:
        list_square3.append(i**2)
print(list_square3)

list_square4 = [i ** 2 for i in range(1,4) if i !=1]
print(list_square4)


# 嵌套循环
list_square5 =[]
for i in range(1,4):
    for j in range(1,5):
        list_square5.append(i*j)
print(list_square5) # [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12]

list_square6 = [i*j for i in range(1,4) for j in range(1,5)]
print(list_square6)
'''
import sys

'''
print("-----------------tuple-----------------------------")
# 元组，不可变特性
tuple_hog = (1,2,3)
print("tuple_hog",tuple_hog)
print(type(tuple_hog))

print(tuple_hog.index(1))
# 不可变特性
# tuple_hog[1]=1 # 会报错
# 元组里面可以嵌套列表，列表的元素可以修改
a = [1,2,3]
tuple_hog2 = (1,2,a)
print(id(tuple_hog2[2])) # 内存地址
tuple_hog2[2][1] = "0"
print(tuple_hog2) # (1, 2, [1, '0', 3])
print(id(tuple_hog2[2]))

# 元组索引，如果有多个重复元素，会给出第一个元素的位置
tuple_hog3 = (1,2,3,"a","b","c","a")
print(tuple_hog3.index("a")) # 3
print(tuple_hog3)
'''
# 集合
'''
print("-----------------set-----------------------------")
a = {1,2,3}
b = {1,4,5}
# 并集
print(a.union(b))
# 交集
print(a.intersection(b))
# 差集
print(a.difference(b)) # {2, 3}
a.add("a")

# 集合的去重功能
print({i for i in "abbddcfld"})
# {'c', 'l', 'd', 'b', 'a', 'f'}

c = "ahbbbdll"
print(set(c))
# {'d', 'h', 'b', 'l', 'a'}
'''
# 字典
'''
print("-----------------dict-----------------------------")
hog_dict = {"a":1,"b":2}
hog_dict2 = dict(a=1,b=2)
print("hog_dict",hog_dict)
# hog_dict {'a': 1, 'b': 2}
print("hog_dict2",hog_dict2)
# hog_dict2 {'a': 1, 'b': 2}

print(hog_dict.keys())
# dict_keys(['a', 'b'])
print(hog_dict2.values())
# dict_values([1, 2])

print(hog_dict.pop("a")) # 1
print(hog_dict) # {'b': 2}
# 返回被删除的键值对
print(hog_dict.popitem()) # ('b', 2)
# 删除掉上面执行的键值对之后，还剩余的元素
print(hog_dict)

a = {}
b = a.fromkeys([1,2,3])
print(b)
# {1: None, 2: None, 3: None}
c = a.fromkeys((1,2,3),"a")
print(c)
# {1: 'a', 2: 'a', 3: 'a'}

print({i:i*2 for i in range(1,3)})
# {1: 2, 2: 4}
'''
# Python模块
'''
print("-----------------module-----------------------------")
import sys
print(sys.argv)
import time
time.sleep(3)
print("exit")

import numpy as np
a = np.arange(15).reshape(3,5) # 获得一个3*5的矩阵
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
print(a)

import mymodule
print(mymodule.add(1,3))
'''

# 字面量
# 文件读取
import os
f = open('mymodule.py','rt')
# print(f.read())
# print(f.readline()) # 第一个函数，打印文件的第一行
# def add(a,b):
# print(f.readline())
# return a + b
# print(f.readlines()) # 以列表显示出来
# ['def add(a,b):\n', '    return a+b\n', '\n']
# f.close()

# 最优方法
# with方法更加优雅，会自动回收资源，不需要close
'''

with open('mymodule.py','rt') as f:
    # print(f.readlines())
# ['def add(a,b):\n', '    return a+b\n', '\n']
    while True:
        line = f.readline()
        if line:
            print(line) # 如果行有内容，就打印出来。这里会出现空行，因为print本身就会带来空行
        else:
            break
'''

# json
"""

print("------------------------json---------------------")
import json
info = [{
    "name":"tom","gender":"male",'other':None},
    {"name":"lucas","gender":"female","other":None
}]
print("读取json文件 ")
# dumps把Python的字典转换为字符串
data = json.dumps(info,sort_keys=True,indent=4)
print(data)
print(type(data))
# <class 'str'>

# 把json内容导入文件
json.dump(info,open("anytest.py",'w'))
print(type(info))
# <class 'list'>
# 以下写法的字符串是不能转换为json的，因为需要双引号，而不是单引号的。
# 报错json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 3 column 31 (char 33)
# str_wrong = '''[{"name":"tom","gender":"male",'other':null}]'''
str = '''[{"name":"tom","gender":"male","other":null}]'''
print(type(str))
# <class 'str'>
# loads把字符串转换为json
data = json.loads(str)
print(type(data))
# <class 'list'>
# print(data)

# load方法把文件打开从字符串转换为json
jsobj = json.load(open('jsontest.json','r'))
print(jsobj)
print(type(jsobj))
print(jsobj[0]['gender'])
# 打印出指定第0个位置的gender键对应的值
"""

print("------------------------异常与错误---------------------")
'''
try:
    num1 = int(input("输入一个除数："))
    num2 = int(input("输入一个被除数："))
    print(num1/num2)
except ZeroDivisionError:
    print("被除数不能为0")
except ValueError:
    print("输入的需要是数值型整数")
except:
    print("这是一个异常")
else:
    print("程序没有发生异常")
finally:
    print("无论是否发生异常，这里都会执行————\n刚刚输入的数值分别是：")
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")


# x = 10
# if x > 5:
#     raise Exception("这是抛出的异常信息")

class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
raise MyException("value1","value2")
# 这里会把自定义的异常给抛出来
'''

# 面向对象编程
print("-------------------面向对象----------------------------------")
'''
class Person():
    name = "noname"

    def get_name(self):
        return self.name # 调用实体本身的方法，需要加一个self

print(Person.name) # noname
# 实例化一个类，用一个变量调用类的属性、方法
P = Person()
print(P.name) # noname
print(P.get_name()) # noname

# 修改实例的属性
P.name = 'lili'
print(P.name) # lili
print(P.get_name()) # lili

# 修改类的属性
Person.name = 'www'
print(P.name) # lili
print(P.get_name()) # lili
# 如果实例已经修改，再去修改类的属性，就无法影响实例
# 实例化之后再修改类，结果还是lili，而不是www。除非这里对实例再修改
P.name = 'wowowo'
print(P.name) # wowowo
print(P.get_name()) # wowowo

print("-------------分割线-----------")
p2 = Person()
print(p2.name) # www
print(p2.get_name()) # www
# 这里是沿用了前面类属性修改后的结果www

# 如果实例化，那么结果跟实例化秀修改的一致
p2.name = 'hhh'
print(p2.name) # hhh
print(p2.get_name()) # hhh

print(Person.name) # www
'''
'''
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f" name : {self.name},gender : {self.gender}, age:{self.age}  我在干饭")

    def drink(self):
        print(f"name : {self.name},gender : {self.gender},age : {self.age} 我在喝水水")

    def set_att(self,value):
        self.value = value

zfj = Person("zfj",25,'female')
cxz = Person("cxz",26,'male')
print(zfj.age)
cxz.set_att("good")
print(cxz.value)
# good
'''

# 回合制游戏
"""

class Game:
    def __init__(self,hp,power): # 将角色的hp、power通过传参传入
        self.hp = hp
        self.power = power

    def fight(self,enermy_hp,enermy_power):
        final_hp = self.hp - enermy_power
        enermy_final_hp = enermy_hp - self.power
        if final_hp > enermy_final_hp:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("我赢了")
        elif final_hp < enermy_final_hp:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("敌人赢了")
        else:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("平局")

"""
后裔，后裔继承了角色的hp\power，还多了一个护甲属性
"""
class Houyi(Game):
    # 如果在子类中重新定义了__init__，那么父类的__init__将会被覆盖
    def __init__(self,):
        super().__init__(hp,power)
        self.defense = 100

    def houyi_fight(self,enermy_hp,enermy_power):
        final_hp = self.hp - enermy_power + self.defense
        enermy_final_hp = enermy_hp - self.power
        if final_hp > enermy_final_hp:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("后裔赢了")
        elif final_hp < enermy_final_hp:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("敌人赢了")
        else:
            print(f"final_hp = {final_hp}")
            print(f"enermy_final_hp = {enermy_final_hp}")
            print("平局")

hp = 1000
power = 200

game = Game(hp,power)
game.fight(2000,200)

houyi = Houyi()
houyi.houyi_fight(enermy_hp=2000,enermy_power=200)

print("--------------这里修改了护甲属性-------------------")
houyi.defense = 1000
houyi.houyi_fight(2000,200)
# 平局
"""














