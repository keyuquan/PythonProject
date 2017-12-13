#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import pandas as pd

# matpltlib 数据可视化库
# 画 折线图 Group picture

# 画组图

unrate = pd.read_csv('unrate.csv')
date = pd.to_datetime(unrate['DATE'])
unrate['DATE'] = pd.to_datetime(unrate['DATE'])  # 把 字符串转化为日期
unrate['MONTH'] = unrate['DATE'].dt.month  # 添加一个 month 的 列

first_twelve = unrate[0:12]
second_twelve = unrate[12:24]

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)  # 分成 3 列 2行 ， 取第 1 个 图
ax1.plot(first_twelve['DATE'], first_twelve['VALUE'])

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(second_twelve['DATE'], second_twelve['VALUE'])

ax2 = fig.add_subplot(2, 2, 3)

plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()
