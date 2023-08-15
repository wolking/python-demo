# coding=utf-8
import numpy as np


def stack():
    """
    将不同数组堆叠在一起，有水平堆叠和垂直堆叠

    通过数组堆叠操作，可以实现数据合并，方便处理，也可以构建特定形状的矩阵，用于矩阵运算或求最优解
    :return:
    """
    a = np.arange(6).reshape(2, 3)
    b = np.arange(6, 12).reshape(2, 3)
    print(a)
    print(b)

    # 水平堆叠
    ab = np.hstack((a, b))
    print(ab)

    # 垂直堆叠
    ab = np.vstack((a, b))
    print(ab)


def split():
    """
    将一个数组拆分成多个小数组，返回形状相同的数组，或者在指定列之后进行分割

    因为数组的第一个轴代表垂直方向，所以水平方向上的拆分，都是从第二个轴开始，r=轴的值/拆分的数量，r必须是整数
    以此类推，垂直方向上拆分后的数组形状(轴值/拆分的数量,后面轴不变)
    :return:
    """
    a = np.arange(18).reshape(2, 9)
    # 沿水平轴拆分成3个数组,每一个数组形状为(2, 3),并返回一个list
    na = np.hsplit(a, 3)
    print(na)
    print(type(na))

    # 在垂直方向拆分为2个数组，每一个数组的形状为(1,9)
    na = np.vsplit(a, 2)
    print(na)
    print(na[0].shape)

    # 三维数组的拆分，因为数组的第一个轴代表垂直方向，所以水平方向上的拆分，都是从第二个轴开始，r=轴的值/拆分的数量，r必须是整数
    a = a.reshape(2, 3, 3)
    # [[[ 0  1  2] [ 3  4  5] [ 6  7  8]]
    #  [[ 9 10 11] [12 13 14] [15 16 17]]]
    # 在水平方向上拆成3个数组,每个数组的形状为(2,1,3)
    # [array([[[ 0,  1,  2]],  [[ 9, 10, 11]]]),
    # array([[[ 3,  4,  5]], [[12, 13, 14]]]),
    # array([[[ 6,  7,  8]], [[15, 16, 17]]])]
    print(a)
    print(np.hsplit(a, 3))
    # 如果拆分不均匀或报错
    # print np.hsplit(a, 2)


def re_shape():
    """
        形状操作，改变数组的形状，即改变数组的维度，常用有ravel()/reshape(),以及转置操作ndarray.T
        ravel()：可以将多维数组改成一维数组，顺序遵守最右索引变化最快，即将数组打平，一行一行往后排，
                比如一个二维数组经过ravel后，第一个元素为[0,0]，第二个则为[0,1]，第三个为[1,0],[1,1],[2,0],[2,1]
                return：返回一个新的数组
        reshape()：改变数组的维度，从一维到多维，从多维到一维，与ravel不同的是，reshape需要指定打平后元素总数
                return：返回一个新的数组

        通过对数组形状的操作，可以重塑数据，使其更符合特定的算法或计算方式，也方便数据的压缩或展开，从多维转换为一维，从一维转换为多维
        """
    arr = np.arange(6).reshape((2, 3))
    print(arr)

    # 将数组打平ravel
    na = arr.ravel()
    print(na)
    print(id(arr))
    print(id(na))

    # 通过reshape修改形状，从（2,3）变为（3,2）
    na = arr.reshape((3, 2))
    print(na)

    # 如果将轴指定为-1 ，则会自动计算，比如第一个轴指定为3，第二个轴指定为-1，根据元素总数6个，计算出第二个轴实际应为2
    print(arr.reshape((3, -1)))


if __name__ == '__main__':
    # stack()
    split()


