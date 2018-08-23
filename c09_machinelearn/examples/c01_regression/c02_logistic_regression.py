#!/usr/bin/python
# encoding: utf-8


# logistic regression 逻辑回归

from __future__ import print_function

from c09_machinelearn.mlfromscratch.supervised_learning import LogisticRegression
from c09_machinelearn.mlfromscratch.utils import Plot
from c09_machinelearn.mlfromscratch.utils import normalize, train_test_split, accuracy_score
from sklearn import datasets


def main():
    # Load dataset
    data = datasets.load_iris()
    X = normalize(data.data[data.target != 0])
    y = data.target[data.target != 0]
    y[y == 1] = 0
    y[y == 2] = 1
    # 形成的数据格式：data（ndarray:shape=(100,4)）-> labels（ndarray:shape=(100,)） seed:是否进行随机分配：  1 不随机分配
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, seed=1)

    clf = LogisticRegression(gradient_descent=True)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    # 画3D 图 ；X_test 的 shape （m,n） n>=3； y_pred 为标签
    Plot().plot_in_3d(X_test, y=y_pred)


if __name__ == "__main__":
    main()
