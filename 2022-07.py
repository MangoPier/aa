#
# a = 'Abc'
# print(type(a))
#
# info ={'name':'zfj','age':25}
# print(info)
#
# t1=[1,2,4]
# print(t1)
#
#
# t2=[1,2,{1.5,9},'12','AA',{1,'A'}]
# print(t2)
#
#
# t3=[]
# for i in t2:
#      if type(i) == int or type(i) == float:
#          t3.append(i)
#
# print(max(t3))
#
# 这里有问题，有多余的数据，待查
# for i in t3:
#     j = 1
#     while j <= len(t3):
#         print(f'第{j}个元素是{i}')
#         j=j+1
#
# print(t3)

# id=1
# age = 25
# name = 'zfj'
# weight = 51.5
# print('你的名字是%s' %name)
# print(f'你的名字是{name},年龄{age}岁，体重{weight}公斤')
# print('学号%04d，明年%d岁' %(id,age+1))
# print('hello\nzfj')
# print('hello\tzfj')
# print('hello',end='\n')
#
# print('hello',end='\t')
# print('Lucas',end=' my baby ')
# # hello	Lucas my baby
# print()
#
# name=input('请输入名字：')
# print('OK，查询中========')
# print('查询完成')

# num=input('请输入数字：')
# print(type(num))
# print(type(int(num)))

# num1=13
# print(float(num1))
# l1=[1,2,3]
# l2=['age','20','name','zfj']
# t1=(1,2,4)
# s1={1,3.5}
# print(tuple(l1))
# print(list(s1))
# print(set(t1))
# str1='[1,23]'
# print(type(eval(str1)))
#
# name,age,GF,friends='Lucas',26,'Monie',('zfj','hmm','hry','psy')
# print(GF)
# print(friends)

# a = 3
# b = a
# b *=10
# print(b)
# # 30
# b *= 4+2
# print(b)
# # 180
# print(a > b)
# # False
# print(not (a > b))
# # True
# c=100
# print(a < b and a < c)
# # TRUE
# print(a > b and a > c)
# # False
# print(a > b or a < c)
# True
#
# print(1 and 0)
# 0
# print(2 and 3)
# 3
#
# print(0 or 1)
# print(0 or 0)
# print(1 and 'zfj')
# print('www' and 'zfj')
# print('zfj' and 0)
# print(1 or 'zfj')
# print('zfj' or 1)
# print(not 0)

# infolist=[]
# name = input('请输入姓名：')
# infolist.append(name) # 这里不能在前面赋值
# print(infolist)
#
# name1 = input('请输入姓名：')
# if name1 in infolist:
#     print('信息已存在')
# else:
#     print('不存在该姓名，录入系统')
#     infolist.append(name1)
#     print(infolist)

# age = int(input('输入年龄: '))
# if age >= 18 and age < 60:
#     print(f'年龄是{age}岁，世界是你们年轻人的')
# elif age >= 60:
#     print(f'年龄是{age}岁，该享天伦之乐')
# else:
#     print(f'年龄是{age}岁，茁壮成长ing')

# pk = 0
# distbotton = input('请输入是否勾选分布表按钮，yes or no: ')
# if distbotton == 'yes' or distbotton == 'y':
#     if pk != 1:
#         print('oracle迁移至高斯，这张表是复制表')
#     else:
#         print('oracle迁移至高斯，这张表是分布表，分布键是主键')
# elif distbotton == 'no' or distbotton == 'n':
#     print('oracle迁移至高斯，这张表是复制表')
# else:
#     print('输入有误，请输入: yes或no，y或n')

# import random
# ra = random.randint(0,100)
# rb = random.randint(0,2)
# # print(ra > rb)
# player = int(input('输入1-100以内的序号：'))
# if player < 100 and player > 0:
#     if player > ra:
#         print(f'你输入的是{player}，电脑输入的是{ra}，你赢了')
#     elif player < ra:
#         print(f'你输入的是{player}，电脑输入的是{ra}，电脑赢了')
#     elif player == ra:
#         print(f'你输入的是{player}，电脑输入的是{ra}，打成了平手')
# else :
#     print(f'你输入的是{player}，请输入1-100以内的数字')

# a = 13
# b = 24
# c = a if a > b else b
# print(c)
# d = a-b if a>b else b-a
# print(d)
#
# i = 0
# while i < 10:
#     i += 1
# print(i)
# 10


# i = 1
# while i <= 10:
#     print(f'这是第{i}个数字：')
#     print(i)
#     i += 1
# 遍历1-10的各个数字

# 计算1-100的累加和
# i = 1
# j = 0
# while i <= 100:
#     j += i
#     i += 1
# print(j)
# 5050

# 计算平均值
# a = int(input('输入数字1：'))
# b = int(input('输入数字2：'))
# c = int(input('输入数字3：'))
# ave = (a+b+c)/3
# print(ave)

# 计算1-100的偶数和
# i = 0
# j = 0
# while i <= 100:
#     j += i
#     i = i + 2
# print(j)
# 2550

# 计算1-100的偶数和
# i = 1
# j = 0
# while i <= 100:
#     if i % 2 == 0:
#         j += i
#     i = i+1
# print(j)
# 2550

# 从一串数据里面找出数字最大值
# data = eval(input('请输入一串数据，接下来我会抽出最大值：'))
# print(data)
# l1= []
# for i in data:
#     if type(i) == int or type(i) == float:
#         l1.append(i)
# print(max(l1))

# a = '[12,2]'
# print(type(eval(a)))
# print(eval(a))

# break
# 计算数据的累计和，累加值上限是1000，接近或达到就停止累计
# i = 1
# j = 0
# max = 100
# while i <= max:
#     if j > 1000:
#         j -= i
#         break
#     elif j < 1000:
#         j += i
#     else:
#         print()
#     i = i + 1
# print(j)
# 989

# continue
# continue前后都要有计数器
# i = 1
# j = 8
# while i <= j:
#     if i == 3:
#         print(f'第{i}次，停下，再继续')
#         i += 1
#         continue
#     print(f'第{i}次')
#     i += 1

# while循环嵌套
# 两个变量分别放在while外面、里面
# j = 0
# max = 3
# while j < max:
#     print(f'这是第{j+1}天')
#     i = 1
#     while i <= 1: # 这个1是设置打印多少次
#         print('加班')
#         i += 1
#     j += 1
'''
这是第1天
加班
这是第2天
加班
这是第3天
加班
'''

# while循环嵌套
# 两个变量都放在外面
# j = 0
# i = 1
# max = 5
# while j < max:
#     print(f'这是第{j+1}天')
#     print(i)
#     while i <= 2: # 这个1是设置打印多少次
#         print('加班')
#         i += 1
#     '''对嵌套的这个while循环来说，第二轮循环时，i 已经不满足while i <=1这个条件了，所以就不会再打印这一行'''
#     j += 1
'''
这是第1天
加班
这是第2天
这是第3天
这是第4天
这是第5天
'''


# 打印5个星星
# 法一
# print('*'*5)
# 法二
# i = 0
# while i < 5:
#     print('*',end='')
#     i += 1

# 打印5行5个星星
# 法一
# j = 0
# while j < 5:
#     i = 0
#     while i < 5:
#         print('*',end='')
#         i += 1
#     print()
#     j += 1


# 打印5行星星，第一行是1个，第二行是2个,最后显示是一个直角三角形
# j = 0
# while j < 5:
#     i = 0
#     while i <= j:
#         print('*',end='')
#         i += 1
#     print()
#     j += 1

# 法二
# i = 0
# while i < 6:
#     print('*' * i )
#     i += 1


# 九九乘法表
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(f'{i} * {j} = {i*j}',end='\t')
#         j = j + 1
#     print()
#     i = i+1

# for 循环
# name='zfj'
# for i in name:
#     print(i,end='  ')

# l1=[1,2,3]
# for i in l1:
#     print(i)
#     if i < max(l1):
#         print('上面这个数字并非最大值')
#     else:
#         print('此时这是最大值')
#         i = i+1

# for+break
# namel1=['zfj','xxj','www','lll']
# for i in namel1:
#     print(i)
#     if i == 'www':
#         print('找到了，停止搜索')
#         break

# for + continue
# 遇到偶数就停下来跳过，计算结果为奇数相加和
# i = 1
# j = 0
# while i <= 10:
#     j += i
#     if i % 2 == 0:
#         j -= i
#         i = i + 1
#         continue
#     i = i + 1
# print(j)
# 25

# i = 1
# j = 10
# q = 0
# while i <= j:
#     q = q + i
#     print(f'第{i}次')
#     while i == 5:
#         i = i + 1
#         continue
#     i = i + 1
# print(q)
# 49，当i=5时有继续计算，进入第二个while循环，i变成6，然后跳出while循环，变成7，参与q的运算。整个运算就忽略了6

# 计算奇数和
# i = 1
# j = 10
# q = 0
# while i <= j:
#     q = q + i
#     print(f'第{i}次')
#     while i % 2 == 1:
#         i = i + 1
#         continue
#     i = i + 1
# print(q)
# 25

# else，下方缩进的代码，指的是当循环正常结束之后要执行的代码.while……else……
# 计算1-100的累计和，完成之后打印数字
# i = 1
# j = 0
# while i <= 100:
#     j += i
#     i += 1
# else:
#     print(j)
# # 5050

# 引入break,后面的循环不再执行，else也不执行了
# 当累加和达到4000就不再继续运算了
# i = 0
# j = 0
# q = 100
# while i <= q:
#     j += i
#     if j > 4000:
#         break
#     i += 1
# else:
#     print(j)
# 这里没有打印

# 引用continue，计算出3的倍数的累加和，else后面的有执行
# i = 0
# j = 0
# while i <= 10:
#     j += i
#     if i % 3 != 0:
#         j = j - i
#         i = i + 1
#         continue
#     i = i + 1
# else:
#     print(j)

# for……else,break/continue
# myname='zfj'
# for i in myname:
#     print(i,end='\t')
#     if i == 'f':
#         # break
#         continue
# else:
#     print()
#     print('--------已完成打印-------')

# \ ，换行符号，转义字符
# 换行
# abc = 'a' \
#     'c'
# print(abc)

# 转义
# juzi = 'I\'m zfj'
# print(juzi)

# lizi = 'zfj' \
#        'hhh'
# print(lizi)
#
# lizi = '''this
# is
# an
# example
# '''
# print(lizi)
# print(lizi[2])
# qiepian = '0123456789'
# print(qiepian[0:9:2])
# # 02468
# print(qiepian[0:3])
# # 012
# print(qiepian[2:])
# # 23456789
# print(qiepian[:7:2])
# # 0246
# print(qiepian[::-1])
# # 9876543210
# print(qiepian[-5:-9:-1])
# # 5432
# print(qiepian[-5:-1:1])
# # 5678

# find
# love = 'my favorite fruit is durian and beloved man is Lucas'
# print(love.find('my'))
# # 0
# print(love.find('is'))
# # 18
# print(love.rindex('is'))
# # 44，从右边开始查找
# print(love.find('Lucas',44,50))
# # -1,在44到50这个区间找不到完整的一个子串数据
# print(love.find('Lucas',44,59))
# # 47
# # index
# print(love.index('is'))
# # 18
# print(love.index('Lucas'))
# # 47
# # count
# print(love.count('is'))
#
# print(love.replace('durian','duriancake'))
# print(love.replace('is','is not',2)) # 替换两次
# split
# lizi1 = love.split('is',1)
# print(lizi1)

# j1 = '   啦啦啦 \n' \
#      '888888888'
# j2 = '--' .join(j1)
# print(j2)
# j3='hhh'.join(j1)
# print(j3)
# print('=='.join('www'))
# # w==w==w
# print('zfj'.capitalize())
# # Zfj
# j4 = '8j8q8k'
# print(j1.join(j4))
# print('ll22'.replace('l','hh',1))
# print(j4.title())
# print(j4.lower())
# print(j4.upper())
#
# print(j1.lstrip())
# print(j1)
# print(j1.rstrip())

# just1 = 'zhao88fj'
# print(just1)
# print(just1.ljust(10,'-'))
# print(just1.rjust(10,'='))
#
# print(just1.startswith('z'))
# print(just1.endswith('f'))
# print(just1.startswith('h',1,2))
# print(just1.isalpha())
# print(just1.isspace())
# print(just1.isalnum())

# str1 = 'wwwlllzzz'
# print('l' in str1)
# # true
# print(len(str1))

# 列表
# ls = [11,'22']
# print(len(ls))
# namelist = ['zfj','www']
# nameinput = input('输入名字：')
# if nameinput in namelist:
#     print('名称已存在')
# else:
#     namelist.append(nameinput)
# print(namelist)

l2 = ['a','bb','ccc']
str1 = 'dddd'
str2 = 'eeee1e'
l2.append(str1)
print(l2)
l2.extend(str2)
print(l2)
print(l2.index('a'))
l2.insert(1,'a1b')
print(l2)

# del str1 # 删除对象
# print(str1)
# 报错

del l2[1]
print(l2)

print(l2.index('a'))
print(l2.count('a'))

print(l2.pop(1))
l2.remove('e')
print(l2)

# 列表嵌套
'''
teachers = ['A','B','C','D','E','F','G','H']
office = [[],[],[]]

import random

for name in teachers:
    num = random.randint(0,2)
    office[num].append(name)

i = 1
for officer in office:
    print(f'办公室的人数是{len(officer)}，老师分别是：')
    for name in officer:
        print(name,end='\t')
    print()
i += 1


'''






