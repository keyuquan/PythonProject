#!/usr/bin/env python
# coding=utf-8

# 2.解决导入循环问题
def print_func():
    print 'in module c05_moudle02 '
    return

import c05_moudle01
if __name__ == '__main__':
    c05_moudle01.print_func()
