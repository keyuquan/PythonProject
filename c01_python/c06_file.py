#!/usr/bin/env python
# coding=utf-8

# 文件的操作
# Python进行文件读写的函数为open或file:
# file_handler = open(filename,, mode）
# open
# mode
# w
# 以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
# a
# 以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
# r + 以读写方式打开文件，可对文件进行读和写操作。
# w + 消除文件内容，然后以读写方式打开文件。
# a + 以读写方式打开文件，并把文件指针移到文件尾。
# b
# 以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。
#
# 操作文件对象方法
# f.close()
# 关闭文件，记住用open()
# 打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
# f.fileno()
# 获得文件描述符，是一个数字
# f.flush()
# 刷新输出缓存
# f.isatty()
# 如果文件是一个交互终端，则返回True，否则返回False。
# f.read([count])
# 读出文件，如果有count，则读出count个字节。
# f.readline()
# 读出一行信息。
# f.readlines()
# 读出所有行，也就是读出整个文件的信息。
# f.seek(offset[, where])    把文件指针移动到相对于where的offset位置。where为0表示文件开始处，这是默认值 ；1
# 表示当前位置；2
# 表示文件结尾。
# f.tell()
# 获得文件指针位置。
# f.truncate([size])
# 截取文件，使文件的大小为size。
# f.write(string)
# 把string字符串写入文件。
# f.writelines(list)
# 把list中的字符串一行一行地写入文件，是连续写入文件，没有换行。

# 例1：从文本文件中每读取一行文本便输出
# !/usr/bin/env/ python
# coding=utf-8

fileHandler = open('/root/a.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)
line = fileHandler.readline()
while line:
    print line
line = fileHandler.readline()
fileHandler.close

# 例2:其他文件IO函数的使用
# !/usr/bin/env/ python
# coding=utf-8

fileHandler = open('/root/a.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)
# 读取整个文件
contents = fileHandler.read()
print contents

# 读取所有行,再逐行输出
fileHandler.seek(0)
lines = fileHandler.readlines()
for line in lines:
    print line

# 当前文件指针的位置
print fileHandler.tell()

fileHandler.close

# 例3:用file(...)
# 替换open(...)
# !/usr/bin/env/ python
# coding=utf-8
fileHandler = file('/root/a.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)
line = fileHandler.readline()
while line:
    print line
line = fileHandler.readline()

# 例4:文件的写操作
# !/usr/bin/env/ python
# coding=utf-8

fileHandler = file('/root/a.txt', 'a+')  # 或者调用open()函数
fileHandler.write("\r\n")
fileHandler.write("thank you")

fileHandler.seek(0)
contents = fileHandler.read()
print contents

fileHandler.close


# 文件夹相关操作
# Python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。
# 得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
# 返回指定目录下的所有文件和目录名:os.listdir()
# 删除一个文件:os.remove()
# 删除多个目录（只能删除空目录）：os.removedirs（r”c：\python”）
# 检验给出的路径是否是一个文件：os.path.isfile()
# 检验给出的路径是否是一个目录：os.path.isdir()
# 判断是否是绝对路径：os.path.isabs()
# 检验给出的路径是否存在:os.path.exists()
# 返回一个路径的目录名和文件名:os.path.split()
# Eg：
#  os.path.split('/home/swaroop/byte/code/poem.txt')
# 结果：('/home/swaroop/byte/code', 'poem.txt')
# 分离扩展名：os.path.splitext()
# 获取路径名：os.path.dirname()
# 获取文件名：os.path.basename()
# 运行shell命令: os.system()
# 读取和设置环境变量:os.getenv() 与os.putenv()
# 给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
# 指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
# 重命名：os.rename（old， new）
# 创建多级目录：os.makedirs（r“c：\python\test”）
# 创建单个目录：os.mkdir（“test”）
# 获取文件属性：os.stat（file）
# 修改文件权限与时间戳：os.chmod（file）
# 终止当前进程：os.exit（）
# 获取文件大小：os.path.getsize（filename）