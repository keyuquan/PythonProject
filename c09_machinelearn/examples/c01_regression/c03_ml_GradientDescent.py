#!/usr/bin/python
# encoding: utf-8
"""
用梯度下降问题解决回归问题
用不断尝试的方法 确定 回归参数中造成的数据差异最小 的参数
即是 确定 关系式子 y = k1*x1+k2*x2+..+kn*xn+e  和 p=1/(1+e^(-(k1*x+k2*x+..+kn*xn+e))) 的参数值
线性回归是 : 假设 E最小的情况下,求使 y的差距和 最小的k 值；所以 线性回归是对 k 的 梯度下降 ,e 已经假设为了最小值

逻辑回归由于,嵌套了 sigmod函数 和 p 和 1-p 大小的比较,所以导数没有0值,即是 方差 无法假设最小值,所以是对 k 和 e 两个参数的梯度下降（不断尝试）

"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Read data from csv
pga = pandas.read_csv("pga.csv")

# Normalize the data
pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()

def cost(theta0, theta1, x, y):
    J = 0
    m = len(x)
    for i in range(m):
        h = theta1 * x[i] + theta0
        J += (h - y[i])**2
    J /= (2*m)
    return J

# Use these for your excerise
theta0s = np.linspace(-2,2,100)
theta1s = np.linspace(-2,2, 100)
COST = np.empty(shape=(100,100))
# Meshgrid for paramaters
T0S, T1S = np.meshgrid(theta0s, theta1s)
# for each parameter combination compute the cost
for i in range(100):
    for j in range(100):
        COST[i,j] = cost(T0S[0,i], T1S[j,0], pga.distance, pga.accuracy)

# make 3d plot
fig2 = plt.figure()
ax = fig2.gca(projection='3d')
ax.plot_surface(X=T0S,Y=T1S,Z=COST)
plt.show()


