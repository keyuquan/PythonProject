#!/usr/bin/env python
# coding=utf-8


# c01_python 语法

#1.行和缩进
#  Python中，不使用括号来表示代码的类和函数定义块或流程控制。
# 代码块是由行缩进，缩进位的数目是可变的，但是在块中的所有语句必须缩进相同的量。
if True:
    print "True"
else:
  print "False"

#2.引号
# Python接受单引号（'），双引号（“）和三（''或”“”）引用，以表示字符串常量，只要是同一类型的引号开始和结束的字符串。
# 三重引号可以用于跨越多个行的字符串。例如，所有下列是合法的：
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is made up of multiple
 lines and sentences paragraph = """

#3.注释
#!/usr/bin/c01_python
#  This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.

#4.分号
# python中一个语句的结束不需要使用分号
# 如果想在一行中输入多个语句，可使用分号
import sys; x = 'foo'; sys.stdout.write(x+"""
""")