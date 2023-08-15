# coding=utf-8
import numpy as np


def index():
    """
    索引：与list相似，不同的是，数组的每一个轴都可以有索引，也可以使用切片的方式，这些索引以逗号分隔的元组给出
    :return:
    """
    # 一维数组
    arr = np.arange(10)
    print arr[1]
    print arr[:5]

    # 多维数组
    """
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    """
    arr = np.arange(20).reshape((4, 5))  # 生成0-20之间的数，变成4行5列的数组
    print arr

    # 获取第2行第4个元素
    print arr[1, 3]     # 8

    # 获取第2-4行，第3列的数据
    # 此处的1:是对行的切片，也是对第一个轴的切片操作
    print arr[1:, 2]    # [ 7 12 17]

    # 当提供的索引少于轴的数量时，缺失的索引会被认为是对缺失的轴的完整切片
    # arr[1]等价于arr[1,:]
    print arr[1]    # [5 6 7 8 9]

    # arr[1,:]也可以写为arr[1,...]
    print arr[1, ...]


def it():
    """
    迭代遍历
    :return:
    """
    # 对第一个轴进行遍历
    arr = np.arange(20).reshape((4, 5))
    for x in arr:
        # x是第二个轴
        print x

    # 对数组所有元素进行遍历,使用flat
    for x in arr.flat:
        print x


if __name__ == '__main__':
    # 索引、切片、迭代
    # index()
    it()
