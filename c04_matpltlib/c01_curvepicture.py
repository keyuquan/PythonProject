#!/usr/bin/env python
# coding=utf-8

import pandas as pd

# matpltlib 数据可视化库

# 画折线图
import matplotlib.pyplot as plt

# ================ 单图
unrate = pd.read_csv('unrate.csv')
date = pd.to_datetime(unrate['DATE'])
unrate['DATE'] = pd.to_datetime(unrate['DATE'])  # 把 字符串转化为日期
unrate['MONTH'] = unrate['DATE'].dt.month  # 添加一个 month 的 列

first_twelve = unrate[0:12]
second_twelve = unrate[12:24]

plt.figure(figsize=(10, 6))  # 画布大小
plt.plot(first_twelve['DATE'].dt.month, first_twelve['VALUE'], c='red', label="1948")  # x.y 坐标的值，颜色，折线标注  决定画折线图
plt.plot(second_twelve['DATE'].dt.month, second_twelve['VALUE'], c='blue', label="1949")
plt.legend(loc='upper left')  # 折线标注的位置
plt.xticks(rotation=90)  # 字体倾斜度
plt.xlim()
plt.ylim()
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()

# ================ 多曲线
fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i * 12
    end_index = (i + 1) * 12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.title('Monthly Unemployment Trends, 1948-1952')

plt.show()

# ================ 组图
women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
cb_dark_blue = (0 / 255, 107 / 255, 164 / 255)
cb_orange = (255 / 255, 128 / 255, 14 / 255)

fig = plt.figure(figsize=(18, 3))

for sp in range(0, 6):
    ax = fig.add_subplot(1, 6, sp + 1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100 - women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)  # 外界边框不可见
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
plt.legend(loc='upper right')
plt.show()
