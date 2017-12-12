#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import numpy as np

# pandas
# Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。
# 你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一

# 一.数据读取
# 读取后的数据类型 pandas.core.frame.DataFrame ，把数据形成一个表，相当于 spark的  DataFrame，便于数据分析
food_info = pd.read_csv("food_info.csv")
print(type(food_info))
print food_info.dtypes
print food_info.columns
print food_info.shape
print food_info.head(5)
print food_info.loc[5]
print food_info.loc[5, "Shrt_Desc"]
print food_info.loc[[2, 5, 10]]
# print  food_info

# 注意： 这两个方法 获取的返回值不一样
# pandas.core.frame.DataFrame ，带源数据，相当于 spark的  DataFrame
# pandas.core.series.Series  ，不带源数据，相当于 spark的 rdd
se1 = food_info[[food_info.columns[0]]]
se2 = food_info[food_info.columns[0]]
print  type(se1)  # pandas.core.frame.DataFrame
print  type(se2)  # pandas.core.series.Series

food_info[[food_info.columns[0], food_info.columns[2], "Ash_(g)"]]
col_names = food_info.columns.tolist()
gram_columns = []
for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head(3))

# 二.对数据的操作
# 1.排序 对DataFrame进行就地排序，而不是返回新的DataFrame(sort_values 的返回值为 none)，数据为"" 的数据为NaN
food_info.sort_values("Sodium_(mg)", inplace=True)
print food_info["Sodium_(mg)"]

food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
print food_info["Sodium_(mg)"]

# 2. 求平均数
titanic_survival = pd.read_csv("titanic_train.csv")
age = titanic_survival["Age"]
print  type(age), age.dtypes  # pandas.core.series.Series ,float64

# 问题：  当存在 非数字数据的时候，运算结果是 NAN
mean_age = sum(titanic_survival["Age"]) / len(titanic_survival["Age"])
print mean_age

# i.原始代码
# 分步代码
age_is_null = pd.isnull(age)
print age_is_null
print  type(age_is_null), age_is_null.dtype  # <class 'pandas.core.series.Series'> bool

age_null_true = age[-age_is_null]  # 所有不是null 的数据 当是 true 的时候，取该数据，当是 false 时，不取该数据
print age_null_true
print  type(age_null_true), age_null_true.dtype  # <class 'pandas.core.series.Series'> float64

age_null_count = len(age_null_true)
print(age_null_count)

# 整合后的代码
age_null_true = titanic_survival["Age"][-pd.isnull(titanic_survival["Age"])]  # 所有不是null 的数据
mean_age1 = sum(age_null_true) / len(age_null_true)
print mean_age1

# ii. pandas提供的api
# we have to filter out the missing values before we calculate the mean.
good_ages = titanic_survival["Age"][age_is_null == False]
# print good_ages
correct_mean_age = sum(good_ages) / len(good_ages)
print correct_mean_age

# iii. pandas提供的方法 mean，已经过滤 非数字数据
correct_mean_age = titanic_survival["Age"].mean()
print correct_mean_age

# 3.分组求平均数,和

# 平均票价原始代码
passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
    pclass_fares = pclass_rows["Fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
print fares_by_class

# 平均票价 pandas 提供方法  pivot_table
# index tells the method which column to group by
# values is the column that we want to apply the calculation to
# aggfunc specifies the calculation we want to perform
passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Fare", aggfunc=np.mean)
print passenger_survival

passenger_age = titanic_survival.pivot_table(index="Pclass", values="Survived")
print(passenger_age)

port_stats = titanic_survival.pivot_table(index="Embarked", values=["Fare", "Survived"], aggfunc=np.sum)
print(port_stats)


# 4.自定义方法
# This function returns the hundredth item from a series
def which_class(row):
    pclass = row['Pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"

classes = titanic_survival.apply(which_class, axis=1)
print classes
# print which_class(titanic_survival) 错误，不能直接调用


# 5.过滤 某些 为null 的数据
# specifying axis=1 or axis='columns' will drop any columns that have null values
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=["Age", "Sex"])
print new_titanic_survival

# 5. 重新排序，不改变原来数据的顺序
new_titanic_survival = titanic_survival.sort_values("Age", ascending=False)
print new_titanic_survival[0:10]

titanic_reindexed = new_titanic_survival.reset_index(drop=True)
print (titanic_reindexed.iloc[0:10])
