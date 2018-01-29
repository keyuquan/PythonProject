#!/usr/bin/python
# encoding: utf-8

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mlfromscratch.utils import train_test_split, standardize, accuracy_score
from mlfromscratch.utils import mean_squared_error, calculate_variance, Plot
from mlfromscratch.supervised_learning import RegressionTree

"""
使用自己定义的决策数训练数据,预测数据值 的决策树
(python 有自己定义的决策树 名字 ：tree)
"""


def main():
    print("-- Regression Tree --")

    # Load temperature data
    data = pd.read_csv('TempLinkoping.txt',
                       sep="\t")

    time = np.atleast_2d(data["time"].as_matrix()).T
    temp = np.atleast_2d(data["temp"].as_matrix()).T

    X = standardize(time)  # Time. Fraction of the year [0, 1]
    y = temp[:, 0]  # Temperature. Reduce to one-dim

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = RegressionTree()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Color map
    cmap = plt.get_cmap('viridis')
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)

    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color='red', s=10)
    m3 = plt.scatter(X_test, y_pred, color='black', s=10)
    plt.suptitle("Regression Tree")
    plt.title("MSE: %.2f" % mse, fontsize=10)
    plt.xlabel('Day')
    plt.ylabel('Temperature in Celcius')
    plt.legend((m1, m2, m3), ("Training data", "Test data", "Prediction"), loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
