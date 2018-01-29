#!/usr/bin/python
# encoding: utf-8

from __future__ import division, print_function
import numpy as np
import pandas as pd
from sklearn import tree
from c07_machinelearn.mlfromscratch.utils import Plot
from c07_machinelearn.mlfromscratch.utils import train_test_split, accuracy_score

"""
根据，身高，体重，腰围 三项数据训练模型，并预测某人胖瘦
"""
def main():
    body_info = pd.read_csv("BodyType.csv")
    X = np.array(body_info[[body_info.columns[0], body_info.columns[1], body_info.columns[2]]])
    labels = np.array(body_info[body_info.columns[3]])
    Y = np.zeros(labels.shape[0])
    Y[labels == 'fat'] = 1

    clf = tree.DecisionTreeClassifier(criterion='entropy')
    x_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(X_test)

    # 准确率
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    Plot().plot_in_3d(X_test, y=y_pred)

if __name__ == "__main__":
    main()
