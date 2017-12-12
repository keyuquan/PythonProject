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
print food_info.loc[[2, 5, 10]]
# print  food_info

# 注意： 这两个方法 获取的返回值不一样
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

# 2. isnull 不是数据类型数据的处理
titanic_survival = pd.read_csv("titanic_train.csv")
age = titanic_survival["Age"]
print  type(age), age.dtypes #pandas.core.series.Series

age_is_null = pd.isnull(age)
print age_is_null
print  type(age_is_null), age_is_null.dtype

age_null_true = age[age_is_null]
print age_null_true
age_null_count = len(age_null_true)
print(age_null_count)

mean_age = sum(titanic_survival["Age"]) / len(titanic_survival["Age"])
print mean_age

# we have to filter out the missing values before we calculate the mean.
good_ages = titanic_survival["Age"][age_is_null == False]
# print good_ages
correct_mean_age = sum(good_ages) / len(good_ages)
print correct_mean_age
