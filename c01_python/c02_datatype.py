#!/usr/bin/env python
# coding=utf-8

# 数据类型
# Python有五个标准的数据类型：
# 1.数字
counter = 100  # 整型
miles = 1000.0  # 浮点
name = "John"  # 字符串

print counter
print miles
print name

# 2.字符串
str = 'Hello World!'  # 字符串在python中本质上是一个字符序列Seq

print str  # 打印整个字符串
print str[0]  # 打印字符串第一个字母
print str[2:5]  # 打印第3到第5个字母
print str[2:]  # 打印从第3个字母到末尾
print str * 2  # 字符串重复2次
print str + "TEST"  # 字符串拼接

# 3.列表
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 打印整个列表
print list[0]  # 打印第一个元素
print list[1:3]  # 打印第二和第三个元素
print list[2:]  # 打印第三个元素到末尾
print list[2:]  # 打印第三个元素到末尾
print list[-2:]  # 打印倒数2个到结尾的元素
print list[:-2]  # 打印开头到倒数2个的元素
print tinylist * 2  # 打印2次
print list + tinylist  # 拼接两个list


# 修改list中的元素
# list[0] = "haha"
# print(list)
#
# # 4.元组
# tuple = ('abcd', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print tuple  # 打印整个元组
# print tuple[0]  # 打印第一个元素
# print tuple[1:3]  #  打印第2、3两个元素
# print tuple[2:]  #
# print tinytuple * 2  # 重复2遍
# print tuple + tinytuple  #  拼接
#
# # 5.字典
# tinydict = {'name': 'john', 'code': 6734}
# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#
# print dict['one']       # Prints value for 'one' key
# print dict[2]           # Prints value for 2 key
# print tinydict          # Prints complete dictionary
# print tinydict.keys()   # Prints all the keys
# print tinydict.values() # Prints all the values
#
# #遍历
# r = {"a": 9, "b": 10}
# print(r)
# for num in r.keys():
#     print(num)
# for num in r.values():
#     print(num)
#
# # ============ 数据类型转换
#
# # 有时候，可能需要执行的内置类型之间的转换。
# # 类型之间的转换，只需使用类名作为函数。
# # int(x[, base])    将x转换为整数。基数指定为base（进制）
# # long(x[, base] )    将x转换为一个长整数。基数指定为base，
# # float(x)
# # 将x转换到一个浮点数。
# # complex(real[, imag])    创建一个复数。
# # str(x)
# # 转换对象x为字符串表示形式。
# # eval(str)
# # 计算一个表达式字符串，并返回一个对象。
# # tuple(s)
# # 把s（序列）转换为一个元组。
# # list(s)
# # 把s（序列）转换为一个列表。
# # set(s)
# # 把 s（序列）转换为一个set集合。
# # dict(d)
# # 转成字典, d必须是（键，值）元组序列。
#
# # 例如：
# a = int('A', 16)
# print(a)
#
# a = tuple(range(1, 10, 2))
# print(a)
#
# b = tuple("hello")
# print b
# c = complex(1, 2)
# print c
#
# x = 1
# e = eval('x+1')
# print e
#
# f = dict([(1, 2), (3, 4), ('a', 100)])
# print f
#
# # 结果为：
# (1, 3, 5, 7, 9)
# ('h', 'e', 'l', 'l', 'o')
# (1 + 2j)
# 2
# {'a': 100, 1: 2, 3: 4}
