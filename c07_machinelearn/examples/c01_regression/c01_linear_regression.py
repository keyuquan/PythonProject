#!/usr/bin/python
# encoding: utf-8

import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

from c07_machinelearn.mlfromscratch.supervised_learning import LinearRegression
from c07_machinelearn.mlfromscratch.utils import mean_squared_error
from c07_machinelearn.mlfromscratch.utils import train_test_split


def main():
    # python 的 mlfromscratch 模块 自带的 生成数据集的 方法  :  n_samples:数据个数 n_features：数据特征数 noise：方差
    # 形成的数据格式：data（ndarray:shape=(100,1)）-> labels（ndarray:shape=(100,)）
    X, y = make_regression(n_samples=1000, n_features=1, noise=50)

    # 把数据分成 训练数据和 测试数据
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01)

    # LinearRegression： 线性回归的 源码类
    # n_iterations: 循环多少次,减小,则运算量减小
    # learning_rate: 每次循环 w 和 e 进行相应放大后 改变的 百分比
    # 要多次尝试 找出最合适的 n_iterations  和 learning_rate （当数据平缓时就是最佳值）
    # 一般情况下 learning_rate=1/n_samples*10  数据找到最佳值比较快

    model = LinearRegression(n_iterations=100, learning_rate=.1/1000)

    # 训练数据
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)  # 训练完成后的 预测 数值和实际数值的差距和

    # 预测数据
    y_pred_line = model.predict(X)

    # 展示数据分类效果
    cmap = plt.get_cmap('viridis')
    # Plot the results
    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(X, y_pred_line, color='black', linewidth=2, label="Prediction")
    plt.suptitle("Linear Regression")
    plt.title("MSE: %.2f" % mse, fontsize=10)
    plt.xlabel('Day')
    plt.ylabel('Temperature in Celcius')
    plt.legend((m1, m2), ("Training data", "Test data"), loc='lower right')
    plt.show()

    # 展示随着 算法将调整权重的训练迭代次数 的增加 ； 求出的最小数据的走势图
    n = len(model.training_errors)
    training, = plt.plot(range(n), model.training_errors, label="Training Error")
    plt.legend(handles=[training])
    plt.title("Error Plot")
    plt.ylabel('Mean Squared Error')
    plt.xlabel('Iterations')
    plt.show()


if __name__ == "__main__":
    main()
