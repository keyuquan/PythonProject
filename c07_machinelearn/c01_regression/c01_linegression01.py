#!/usr/bin/python
# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets


# line regression 线性回归
# 场景 ： datasets.load_diabetes()  生成内置的数据集（datasets 内置很多默认的数据集）
# 需求 ： 根据两个属性给数据分类
# 局限性 ：只给两个属性的数据分类，具有局限性

class LinearRegression():
    def __init__(self):
        self.w = None

    # 训练数据： 找出 x y 最合适的关系
    def fit(self, X, y):
        X = np.insert(X, 0, 10, axis=1)
        X_ = np.linalg.inv(X.T.dot(X))
        self.w = X_.dot(X.T).dot(y)

    # 预测数据： 根据 x 和训练的数据  预测 y
    def predict(self, X):
        X = np.insert(X, 0, 10, axis=1)
        y_pred = X.dot(self.w)
        return y_pred


# 实际 Y  和 理论 Y 算出的 差距 平方 的平均值:  方差
def mean_squared_error(y_true, y_pred):
    mse = np.mean(np.power(y_true - y_pred, 2))
    return mse


def main():
    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()

    # 选取其中两个属性
    X = diabetes.data[:, np.newaxis, 2]
    Y = diabetes.data[:, np.newaxis, 3]

    # 把数据分为 训练数据（先验数据，用于确定模型） 和 测试数据（测试模型的准确性）
    x_train, x_test = X[:-20], X[-20:]
    y_train, y_test = Y[:-20], Y[-20:]

    clf = LinearRegression()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)

    # Print the mean squared error 打印均方误差
    print ("Mean Squared Error:", mean_squared_error(y_test, y_pred))

    # Plot the results
    plt.scatter(x_test, y_test, color='black')
    plt.plot(x_test, y_pred, color='blue', linewidth=3)
    plt.show()


main()
