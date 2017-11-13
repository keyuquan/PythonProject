#!/usr/bin/env python
# coding=utf-8

# 模块和包
# 一个文件就是一个模块,一个文件夹就是一个包
# 每个目录下都有__init__.py文件，这个是初始化模块，from-import语句导入子包时需要它，可以在里面做一些初始化工作，也可以是空文件。
# ps：__init__.py定义的属性直接使用 顶层包.子包 的方式导入，如在目录a的__init__.py文件中定义init_db()方法，调用如下：
# from 02_python import c01_grammar.py
# a.init_db()

# 1.导入模块和包的方式
import numpy as np

print np.version.version


# import  numpy._globals
# from numpy import   _globals as gl

# 2.解决导入循环问题
def print_func():
    print 'in module c05_moudle01 '
    return
"""
当该脚本直接被解释执行时，其内置变量__name__的值会被python执行器赋值“__main__”
而如果该脚本是被别的脚本作为模块导入时，__name__的值就不会等于“__main__”
所以，如果不想让别的脚本导入本模块时执行的代码，就可以用如下方式处理：
"""

# # 错误方法
# import c05_moudle02
# if __name__ == '__main__':
#     print 'hello,I m c05_moudle01'

# 在这里a尝试导入b，而b也尝试导入a，导入一个先前没有完全导入的模块，会导致导入失败。解决办法：移除一个导入语句，把导入语句放到函数内部，在需要的时候导入。
if __name__ == '__main__':
    print __name__
    import c05_moudle02
    c05_moudle02.print_func()
else:
    print __name__