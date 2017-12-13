#!/usr/bin/env python
# coding=utf-8
import pandas as pd
from pandas import Series

# Series
# 键值对的数据存储格式，默认键是角标
# 1.Series 和数组相互转化
fandango = pd.read_csv('fandango_score_comparison.csv')
print fandango[[0, 5]], type(fandango[[0, 5]])  # pandas.core.frame.DataFrame
series_film = fandango['FILM']
print series_film[0:5], type(series_film[0:5])  # pandas.core.series.Series
series_rt = fandango['RottenTomatoes']
print series_rt[0:5], type(series_rt[0:5])  # pandas.core.series.Series

film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'].values)
series_one = series_custom[['Minions (2015)', 'Leviathan (2014)']]
series_two = series_custom[[0, 1]]

print film_names, type(film_names)
print rt_scores, type(rt_scores)  # numpy.ndarray
print type(series_custom)  # pandas.core.series.Series
print series_custom
print series_one, type(series_one)  # pandas.core.series.Series
print series_two, type(series_two)  # pandas.core.series.Series

# 2.numpy 对  Series 的操作
# TSeries对象中的值被视为ndarray，即NumPy中的核心数据类型
import numpy as np

# Add each value with each other
print np.add(series_custom, series_custom), type(np.add(series_custom, series_custom))
# Apply sine function to each value
print  np.sin(series_custom), type(np.sin(series_custom))  # pandas.core.series.Series
# Return the highest value (will return a single value not a Series)
print  np.max(series_custom), type(np.max(series_custom))  # numpy.int64

# 3. Series  排序
# 根据索引排序的推导
original_index = series_custom.index.tolist()
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)

print original_index, type(original_index)  # list
print sorted_index, type(sorted_index)  # list
print sorted_by_index, type(sorted_by_index)  # pandas.core.series.Series

# Series 提供的 api :根据索引排序
sc2 = series_custom.sort_index()
# Series 提供的 api :根据值排序
sc3 = series_custom.sort_values()

print sc2, type(sc2)  # pandas.core.series.Series
print sc3, type(sc3)  # pandas.core.series.Series

# 4. Series 求平均值 平均值求得是 值的平均值，不是键的平均值; 最大，追小值
print  fandango["RottenTomatoes"].mean()
print  series_custom.mean()
print  series_custom.max()
print  series_custom.min()

# 5. series 的参数可以是 根据值确定的boolean 值，false 则过滤掉
series_greater_than_50 = series_custom[series_custom > 50]
both_criteria_xiaoyu_75 = series_custom[series_custom < 75]
both_criteria = series_custom[(series_custom > 50) & (series_custom < 75)]

print  len(series_custom)
print  len(series_greater_than_50)
print  len(both_criteria_xiaoyu_75)
print  len(both_criteria)

age_null_true = fandango["RottenTomatoes"][-pd.isnull(fandango["RottenTomatoes"])]  # 所有不是null 的数据
mean_age1 = sum(age_null_true) / len(age_null_true)

series_one = series_custom[['Minions (2015)', 'Leviathan (2014)']]
series_two = series_custom[[0, 5]]
series_thr = series_custom[0:5]
series_greater_50 = series_custom[series_custom == 50]

print  "===================================="
print  series_one
print  series_two
print  series_thr
print  series_greater_50

# 6.求两列 的平均值
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users) / 2
# print   rt_mean
