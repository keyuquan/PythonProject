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
    X, y = make_regression(n_samples=100, n_features=1, noise=20)

    # 把数据分成 训练数据和 测试数据
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    # 线性回归的 源码类
    model = LinearRegression(n_iterations=1000)

    # 训练数据
    model.fit(X_train, y_train)

    # Training error plot
    n = len(model.training_errors)
    training, = plt.plot(range(n), model.training_errors, label="Training Error")
    plt.legend(handles=[training])
    plt.title("Error Plot")
    plt.ylabel('Mean Squared Error')
    plt.xlabel('Iterations')
    plt.show()

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print ("Mean squared error: %s" % (mse))

    y_pred_line = model.predict(X)

    # Color map
    cmap = plt.get_cmap('viridis')

    # Plot the results
    m1 = plt.scatter(366 * X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(366 * X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(366 * X, y_pred_line, color='black', linewidth=2, label="Prediction")
    plt.suptitle("Linear Regression")
    plt.title("MSE: %.2f" % mse, fontsize=10)
    plt.xlabel('Day')
    plt.ylabel('Temperature in Celcius')
    plt.legend((m1, m2), ("Training data", "Test data"), loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
