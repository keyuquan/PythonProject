#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Linear Regression Example
=========================================================
This example uses the only the first feature of the `diabetes` dataset, in
order to illustrate a two-dimensional plot of this regression technique. The
straight line can be seen in the plot, showing how linear regression attempts
to draw a straight line that will best minimize the residual sum of squares
between the observed responses in the dataset, and the responses predicted by
the linear approximation.

The coefficients, the residual sum of squares and the variance score are also
calculated.


=========================================================
线性回归示例
=========================================================
这个例子只使用了'糖尿病'数据集的第一个特征
为了说明这种回归技术的二维图。该
在图中可以看到直线，显示线性回归的尝试方式
画一条直线，最大限度地减少残差平方和
在数据集中观察到的响应与预测的响应之间
线性近似。

系数，残差平方和和方差分数也是计算。

"""
print(__doc__)

# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# 加载糖尿病数据
diabetes = datasets.load_diabetes()

# 只选取其中一个特征的数据
diabetes_X = diabetes.data[:, np.newaxis, 2]

# 把数据切分为 训练集 、测试集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 把标签 切分为  训练集、测试集
diabetes_Y_train = diabetes.target[:-20]
diabetes_Y_test = diabetes.target[-20:]

# 创建线性回归对象
regr = linear_model.LinearRegression()

# 使用训练集训练数据
regr.fit(diabetes_X_train, diabetes_Y_train)

# 预测测试集数据
diabetes_Y_pred = regr.predict(diabetes_X_test)

# Coefficients 系数
"""
下是一组用于回归的方法，其中目标值应该是输入变量的线性组合。在数学概念中，如果 是预测值。
y(w,x)=w0 + w1x1+ w2x2 +..+wpxp
在整个模块中，我们指定了向量 w=(w0,w1,w2,..,wn) 作为 coef_  , w0 作为intercept_
"""
print('系数: \n', regr.coef_)

# 均方误差
print("均方误差:%.2f" % mean_squared_error(diabetes_Y_test, diabetes_Y_pred))

# 解释方差分数：1是完美预测
print('解释方差分数: %.2f' % r2_score(diabetes_Y_test, diabetes_Y_pred))

# 图像化展示
plt.scatter(diabetes_X_test, diabetes_Y_test, color='black')
plt.plot(diabetes_X_test, diabetes_Y_pred, color='blue')
plt.show()
