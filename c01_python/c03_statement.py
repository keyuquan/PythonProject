#!/usr/bin/env python
# coding=utf-8

# 流程控制语句
# 1.if else
#if的条件可以是数字或字符串或者布尔值True和False（布尔表达式）
#如果是数字，则只要不等于0，就为true
#如果是字符串，则只要不是空串，就为true
var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"



# 2. while
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

# 3.for
r = {"a": 9, "b": 10}
print(r)
for num in r.keys():
    print(num)
for num in r.values():
    print(num)
#
#
#
#
#
# if