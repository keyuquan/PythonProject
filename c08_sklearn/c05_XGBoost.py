#!/usr/bin/python
# encoding: utf-8
# XGBoost  集成学习方法

from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

# read in the iris data
iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 训练模型
#  max_depth ：int 基础学习者的最大树深度
#  learning_rate : 集成学习
#  n_estimators ：  适合增强树木的数量
#  silent ：是否在运行增强功能时打印消息
#  multi:softmax ： 指定学习任务和相应的学习目标或 要使用的自定义目标函数
model = xgb.XGBClassifier(max_depth=5, learning_rate=0.9, n_estimators=160, silent=True, objective='multi:softmax')
model.fit(X_train, y_train)

# 对测试集进行预测
ans = model.predict(X_test)

# 计算准确率
cnt1 = 0
cnt2 = 0
for i in range(len(y_test)):
    if ans[i] == y_test[i]:
        cnt1 += 1
    else:
        cnt2 += 1

print("Accuracy: %.2f %% " % (100 * cnt1 / (cnt1 + cnt2)))

# 显示重要特征
plot_importance(model)
plt.show()
