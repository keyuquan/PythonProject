#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 01.reqdemo.py
@time: 2015/12/10 0010 下午 3:07
"""

import requests
# "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
# header:防止反爬虫    User-Agent：网页》右键审查元素》network》User-Agent
header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
response = requests.get('https://www.douban.com',headers=header)
print response.text

print response.content.decode('gbk')