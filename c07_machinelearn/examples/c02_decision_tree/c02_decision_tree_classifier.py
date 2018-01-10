#!/usr/bin/python
# encoding: utf-8

from sklearn import datasets
from sklearn import tree

from c07_machinelearn.mlfromscratch.supervised_learning import ClassificationTree
from c07_machinelearn.mlfromscratch.utils import Plot
from c07_machinelearn.mlfromscratch.utils import train_test_split, accuracy_score

"""
使用自己定义的决策数训练数据,预测数据类型（标签）的决策树
(python 有自己定义的决策树 名字 ：tree)
"""

def main():
    print ("-- Classification Tree --")

    data = datasets.load_iris()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    clf = ClassificationTree()
    clf.fit(X_train, y_train)
    tree.export_graphviz(clf, out_file= open("tree_iris.dot", 'w'))

    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print ("Accuracy:", accuracy)
    Plot().plot_in_3d(X_test, y=y_pred)

    # Plot().plot_in_2d(X_test, y_pred,
    #     title="Decision Tree",
    #     accuracy=accuracy,
    #     legend_labels=data.target_names)


if __name__ == "__main__":
    main()
