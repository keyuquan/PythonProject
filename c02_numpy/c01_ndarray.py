#!/usr/bin/env python
# coding=utf-8
import numpy as np

# 一.ndarray(多维数组)简介
# Numpy中，最重要的数据结构
# ndarray由两部分组成：
# 	实际所持有的数据
# 	描述这些数据的元数据（metadata）


# 基本属性
# ndarray.ndim：数组的维数，也称为rank
# ndarray.shape：数组各维的大小，对一个n行m列的矩阵来说， shape 为 (n,m)
# ndarray.size：元素的总数。
# ndarray.dtype：每个元素的类型，可以是numpy.int32, numpy.int16, and numpy.float64等
# ndarray.itemsize：每个元素占用的字节数。
a = np.arange(15).reshape(3, 5)
print  a.ndim, a.shape, a.size, a.dtype, a.itemsize


# 索引和切片  其中冒号 （:）  就是 该维度的所有数据
print  a, a[1, :]
print  a, a[:, 1]

b = np.arange(60).reshape(3, 4, 5)
print  b, b[1, 2, 3]
print  b
print  b[:, :, 1]


# 数组内部计算
print  a
print a.sum(axis=0)  # 每行和
print a.cumsum(axis=0)  # 每行累计和
print a.sum(axis=1)  # 每列和
print a.cumsum(axis=1)  # 每列累计和
print np.sum(a, axis=0)

# 数组间的运算 : 数组的shape 必须一致
a = np.arange(15).reshape(3, 5)
b = np.ones((3, 5)) * 2
c = a - b
c = a + b
c = a * b
c = a / b
print  a
print  b
print  c

# 矩阵的遍历
for c in a:
    for row in c:
        print  row

# 二. np 常用方法总结
# 基本
a = np.arange(15).reshape(3, 5)
print   np.array([1, 2, 3, 4])
print   np.eye(3)  # 本方法只有一个参数  形成 3行 3列的矩阵
print   np.ones((3, 4))
print   np.zeros((3, 4))
print   np.linspace(0, 10, 30)  # 1到10 均等分为 30份
print   np.random.random((2, 3))  # 随机数



# 改变矩阵的形状(shape)
# reshape 更改数组的形状：不改变数组本身
# resize  更改数组形状：改变数组本身  只有该方法改变数组本身
d = np.arange(15)
print  d
print  d.reshape(3, 5)
print  d
print  d.resize(3, 5)
print  d
print  np.ravel(a)  # 扁平化
print  a.ravel()
print  np.transpose(a)  # 转置
print  a.transpose()

# 合并数组：vstack（垂直方向）和hstack（水平方向）
a = np.arange(15).reshape(3, 5)
b = np.eye(5)
c = np.vstack((a, b))
print  a
print  b
print  c

# 深copy 和  浅copy
# 深copy：创建新的地址值，把数据copy到该地址，两个数据的变化互不影响
a = np.arange(15).reshape(3, 5)
b = a.copy()
print  id(a), id(b), a is b

# 浅copy（=）:b指向a的地址值，两个变量的值同时改变（java 语言中  =  号复写，使用的是深copy）
c = np.arange(15).reshape(3, 5)
d = c
print  id(c), id(d), c is d
