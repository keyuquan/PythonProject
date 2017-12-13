#!/usr/bin/env python
# coding=utf-8

import pandas as pd

# matpltlib 数据可视化库

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))
