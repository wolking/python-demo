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
    a *= b  # [ 0  4 10]
    print a
    print id(a)  # 内存地址不变


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
    根据矩阵乘法运算
    [
        [1*3+2*3=9, 1*4+2*5=14]
        [1*3+3*3=12, 1*4+3*5=19]
    ]
    """
    print a.dot(b)


if __name__ == '__main__':
    # 数组运算
    # normal()
    matrix()
