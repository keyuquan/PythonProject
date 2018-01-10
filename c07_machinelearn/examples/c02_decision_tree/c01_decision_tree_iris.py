#!/usr/bin/python
# encoding: utf-8

"""
这是个数据分析的案例,方便从直观熵寻找,不同种类时间区分较大的维度
场景和需求：根据 鸢尾花 不同 部分的特征数据（萼片长 宽；花瓣 长宽）,找出最能区分鸢尾花 的 特征数据,
即是： 确定某种 鸢尾花  种类,在哪个特征情况下 熵值最小

"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris_data = pd.read_csv('iris.data')
iris_data.columns = ['sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm', 'class']
iris_data.head()

k=sns.pairplot(iris_data.dropna(), hue='class')
plt.show()

plt.figure(figsize=(10, 10))
for column_index, column in enumerate(iris_data.columns):
    if column == 'class':
        continue
    plt.subplot(2, 2, column_index + 1)
    sns.violinplot(x='class', y=column, data=iris_data)
plt.show()
