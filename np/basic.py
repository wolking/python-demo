# coding=utf-8
import numpy as np


def init_array():
    """
    创建一个数组
    :return:
    """
    # 通过其他序列对象直接创建，元素类型根据原序列对象推导
    arr = np.array([1, 2])

    # 数组是大小可知，元素未知的，为了避免数组增长，可通过创建具有初始占位符，类型为float64的数组

    # nparray.zeros()：创建元素均为0.0，类型为float64的数组，入参是一个元组，为数组的shape
    arr = np.zeros((1, 2))
    print arr

    # nparray.ones():与zeros()相同，不同的是，元素均为1.0
    arr = np.ones((2, 3))
    print arr

    # nparray.empty():与上面两个相似，元素则是随机的，取决于内存的状态
    arr = np.empty((4, 5))
    print arr

    # nparray.arange(start, end, interval):类似于range()函数
    # start:起始
    # end:结束
    # interval:间隔，
    arr = np.arange(1, 10, 2)
    print arr

    # nparray.linspace():与arange()相似，但第三个参数被设置为生成的数组长度
    arr = np.linspace(1, 10, 5)
    print arr


def arr_info():
    """
       ndarray:一个大小可知，不可改变的数组
       轴：数组的维度，二维有2个轴，三维有3个轴，轴有长度，为每一个维度的元素个数，
           比如[1, 2, 3]是一个一维数组，只有1个轴，长度为3,[[1,2],[2,3]]是一个二维数组，有2个轴，每一个轴的长度为2
    """

    # 获取数组的轴（维度）,一个数值
    arr = np.array([1, 2, 3])
    print arr.ndim

    # 获取数组的维度,但是一个整数的元组，如：(2L, 2L)，L表示整数为长整型
    # 表示每一个维度中的数组大小，也是每一个轴的长度，比如第一个元素表示数组第一个轴长度为2，第二个轴长度为2
    # 该元组的长度就等于ndim
    arr = np.array([[1, 2], [2, 3]])
    print arr.shape

    # ndarray.size：数组元素的总数，4
    print arr.size


if __name__ == '__main__':
    # arr_info()
    init_array()
