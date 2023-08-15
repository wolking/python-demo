# coding=utf-8
import numpy as np


def normal():
    """
    普通运算，加减乘，与常规的加减乘一致，要求运算的数组的维度必须相同，运算的结果是数组索引相同的元素进行运算后组成的数组
    :return:
    """
    a = np.arange(3)
    b = np.arange(3, 6)
    print a  # [0 1 2]
    print b  # [3 4 5]
    print a + b  # [3 5 7]
    print b - a  # [3 3 3]
    print a * b  # [ 0  4 10]

    # 对于+=、*=等操作，会直接修改被操作的数组，而不会创建新的数组
    print id(a)
    a += b
    print a  # [3 5 7]
    print id(a)  # 内存地址不变
    a *= b  # [ 9 20 35]
    print a
    print id(a)  # 内存地址不变

    # 计算数组元素之和
    print a.sum()  # 64
    print b.sum()  # 12

    # 计算数组中最大最小的元素
    print a.max()  # 35
    print a.min()  # 9

    # 与数值进行运算,相当于该数值与每一个元素做运算
    arr = np.arange(6).reshape((2, 3))
    print 2*arr


def matrix():
    """
    矩阵运算，使用@或dot()函数进行矩阵运算
    @运算符只在python>=3.5才支持
    :return:
    """
    a = np.array([[1, 2],
                  [1, 3]])
    b = np.array([[3, 4],
                  [3, 5]])
    """
    根据矩阵乘法运算,行乘列之和
    [
        [1*3+2*3=9, 1*4+2*5=14]
        [1*3+3*3=12, 1*4+3*5=19]
    ]
    """
    print a.dot(b)


def axis():
    """
    沿数组的轴进行操作，比如行操作，列操作
    axis=0：列操作
    axis=1：行操作
    :return:
    """

    arr = np.array([[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])

    # 对每一列进行求和操作
    print arr.sum(axis=0)  # [ 9 12 15]
    # 对每一行求和
    print arr.sum(axis=1)  # [ 3 12 21]

    # 求每一列最大、最小值
    print arr.max(axis=0)  # [6 7 8]
    print arr.min(axis=0)  # [0 1 2]

    # 对每一行进行累加
    """
    [[0, 0+1, 0+1+2],
   [3, 3+4, 3+4+5],
   [6, 6+7, 6+7+8]]
    """
    print arr.cumsum(axis=1)


def ufunc():
    """
    通函数，numpy提供一些数学函数，比如sin/cos/exp，这些函数会对数组的每一个函数进行运算，输出一个新的数组
    :return:
    """
    arr = np.arange(4)
    # sin
    print np.sin(arr)

    # sqrt 开平方
    print np.sqrt(arr)

    # exp e的n次方
    print np.exp(arr)

    # 更多函数：https://numpy.org/devdocs/reference/routines.logic.html


if __name__ == '__main__':
    # 数组运算
    normal()
    # matrix()
    # axis()
    # ufunc()
