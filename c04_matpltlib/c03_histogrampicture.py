#!/usr/bin/env python
# coding=utf-8

# 柱状图
import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd

####################  竖直图
reviews = pd.read_csv('fandango_scores.csv')
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[num_cols]

print  type(norm_reviews)  # pandas.core.frame.DataFrame

bar_heights = norm_reviews.loc[0, num_cols].values
# print   norm_reviews.ix[0]
bar_positions = arange(5) + 0.75
tick_positions = range(1, 6)
fig, ax = plt.subplots()
# pyplot 和   AxesSubplot=plt.subplots() 的区别：
# pyplot 主画布，AxesSubplot次要画布； 主画布只有一块，次画布可以有一块 和 多块；两个用法基本一致
# print  type(fig),type(ax) #<class 'matplotlib.figure.Figure'> <class 'matplotlib.axes._subplots.AxesSubplot'>

ax.bar(bar_positions, bar_heights, 0.5)  # 柱宽占宽比例  决定画的是柱状图
ax.set_xticks(tick_positions)  # 下标的位置
ax.set_xticklabels(num_cols, rotation=45)  # 下标内容和旋转度

ax.set_xlabel('Rating Source')
ax.set_ylabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()

####################  横向图

bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1, 6)
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_widths, 0.5)  # 横向展示
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel('Rating Source')
ax.set_xlabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
plt.show()

####################  组图
fig = plt.figure(figsize=(5, 10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.bar(bar_positions, bar_heights, 0.5)  # 柱宽占宽比例
ax1.set_xticks(tick_positions)  # 下标的位置
ax1.set_xticklabels(num_cols, rotation=45)  # 下标内容和旋转度

ax1.set_xlabel('Rating Source')
ax1.set_ylabel('Average Rating')
ax1.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

ax2.bar(bar_positions, bar_heights, 0.4)  # 柱宽占宽比例
ax2.set_xticks(tick_positions)  # 下标的位置
ax2.set_xticklabels(num_cols, rotation=45)  # 下标内容和旋转度

ax2.set_xlabel('Rating Source')
ax2.set_ylabel('Average Rating')
ax2.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()
