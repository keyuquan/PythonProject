#!/usr/bin/python
# encoding: utf-8
#  K-Means

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = np.random.normal(0, 2, 1000)
y = np.random.normal(0, 2, 1000)

x1 = np.random.normal(10, 1, 100)
y1 = np.random.normal(10, 1, 100)

x = np.append(x, x1)
y = np.append(y, y1)

x = np.append(x, y)
X = x.reshape(1100, 2)

# 画产生的点
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], s=5)

y_pred = KMeans(n_clusters=2, random_state=170).fit_predict(X)

# 画预测的数据
plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], s=5, c=y_pred)

plt.show()
