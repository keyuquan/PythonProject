#!/usr/bin/python
# encoding: utf-8

"""
这个类对比 LogisticRegression 不同的C 值（正规化强度逆），对于 不同 惩罚（ l1 或 l2）  建立 回归模型的效果
"""

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()

X, y = digits.data, digits.target
X = StandardScaler().fit_transform(X)

# classify small against large digits
y = (y > 4).astype(np.int)

# Set regularization parameter
for i, C in enumerate((100, 1, 0.01)):
    #  i,C 的值  0,100 ; 1,1 ;  2,0 , 0.01 ;
    """ 
    C:正规化强度逆;必须是积极的浮动。较小的值指定更强正规化建设
    penalty: 惩罚, l1 或 l2 ： L1一般用于特征的稀疏化（过滤掉不需要的特征），L2 一般用于防止过拟合。
       密集向量和稀疏向量的区别：
       密集向量的值就是一个普通的Double数组 而稀疏向量由两个并列的 数组indices和values组成
       例如：向量(1.0,0.0,1.0,3.0)
       用密集格式表示为[1.0,0.0,1.0,3.0]，
       用稀疏格式表示为(4,[0,2,3],[1.0,1.0,3.0]) 第一个4表示向量的长度(元素个数)，[0,2,3]就是indices数组，[1.0,1.0,3.0]是values数组 表示向量0的位置的值是1.0，2的位置的值是1.0,而3的位置的值是3.0,其他的位置都是0
    tol：容忍停止标准
    """
    clf_l1_LR = LogisticRegression(C=C, penalty='l1', tol=0.01)
    clf_l2_LR = LogisticRegression(C=C, penalty='l2', tol=0.01)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)

    coef_l1_LR = clf_l1_LR.coef_.ravel()
    coef_l2_LR = clf_l2_LR.coef_.ravel()

    # coef_l1_LR contains zeros due to the
    # L1 sparsity inducing norm

    sparsity_l1_LR = np.mean(coef_l1_LR == 0) * 100
    sparsity_l2_LR = np.mean(coef_l2_LR == 0) * 100

    print("C=%.2f" % C)
    print("Sparsity with L1 penalty: %.2f%%" % sparsity_l1_LR)
    print("score with L1 penalty: %.4f" % clf_l1_LR.score(X, y))
    print("Sparsity with L2 penalty: %.2f%%" % sparsity_l2_LR)
    print("score with L2 penalty: %.4f" % clf_l2_LR.score(X, y))

    l1_plot = plt.subplot(3, 2, 2 * i + 1)
    l2_plot = plt.subplot(3, 2, 2 * (i + 1))
    if i == 0:
        l1_plot.set_title("L1 penalty")
        l2_plot.set_title("L2 penalty")

    l1_plot.imshow(np.abs(coef_l1_LR.reshape(8, 8)), interpolation='nearest', cmap='binary', vmax=1, vmin=0)
    l2_plot.imshow(np.abs(coef_l2_LR.reshape(8, 8)), interpolation='nearest', cmap='binary', vmax=1, vmin=0)
    plt.text(-8, 3, "C = %.2f" % C)

    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    l2_plot.set_xticks(())
    l2_plot.set_yticks(())

plt.show()
