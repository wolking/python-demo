# coding=utf-8
import sys  # 引入一个模块

from func import undefined_param_length2  # 从指定模块中导入指定部分
from list import *  # 从指定模块导入所有内容
import comprehension

from pkg import demo  # 从其他包导入一个模块
from pkg.demo import impt_test  # 从其他包的指定模块导入一个函数

if __name__ == '__main__':
    # 导入其他模块，通过修改模块的__name__属性，可以在导入时执行一些代码，以导入当前目录list模块为例

    # sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表，列表第一个元素通常是当前目录
    print sys.path

    # 通过Python内置dir()函数可以找到指定模块内定义的所有名称
    print dir(comprehension)

    demo.impt_test()
    impt_test()

    # 使用其他模块的函数
    undefined_param_length2(a=1, b=2)
