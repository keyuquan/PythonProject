#!/usr/bin/python
# encoding: utf-8
# LightGBM
import lightgbm as lgb
from sklearn import datasets
from sklearn.model_selection import train_test_split

# 加载iris数据集
iris = datasets.load_iris()

X = iris.data
y = iris.target

print('Sample num: ', len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 模型初始化并训练
clf = lgb.LGBMClassifier(boosting_type='gbdt', num_leaves=31, max_depth=7, learning_rate=0.1,subsample_for_bin=5000)

clf.fit(X_train, y_train)

# 预测结果
ans = clf.predict(X_test)

# 计算准确率
cnt1 = 0
cnt2 = 0
for i in range(len(y_test)):
    if ans[i] - y_test[i] < 1:
        cnt1 += 1
    else:
        cnt2 += 1

print("Accuracy: %.2f %% " % (100 * cnt1 / (cnt1 + cnt2)))