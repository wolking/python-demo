import numpy as np

if __name__ == '__main__':
    """
    NumPy的广播机制是为了解决在不同形状的数组之间进行运算困难的问题
    广播broadcasting描述了numpy在处理不同形状的数组之间算术运算的方式，
        正常情况下，numpy不能很好处理不同形状数组的运算，一般要求数组形状相同，
        要解决这个问题，需要将较小的数组进行扩展，使得该数组与较大数组形状相同。
        所谓的较大数组指的是维度更大的数组，比如(2,3)与(2,2,3)，较大数组指的是(2,2,3)
    数组能否广播必须从数组的最高维向最低维看去(axis↓)，依次对比两个要进行运算的数组的axis的数据宽度是否相等，
        如果在某一个axis下，一个数据宽度为1，另一个数据宽度不为1，那么numpy就可以进行广播；
        但是一旦出现了在某个axis下两个数据宽度不相等，并且两者全不为1的状况，就无法广播。
    更通俗来讲，在两个数组上运算时，NumPy会逐元素地比较它们的形状。它从尾随尺寸开始，并向前发展，如果较小数组从尾开始，尺寸不匹配，
        则会报错：ValueError: operands could not be broadcast together
        比如a.shape=(2,3),b.shape=(2,2),两者运算会报错
    正确举例：
        a = [[0,1,2],[3,4,5]]
        b = [10,20,30]
        a与b是不同形状的两个数组，两者进行运算，将b扩展为[[10,20,30],[10,20,30]]，形状与a相同，运算结果为
        [[10 21 32] [13 24 35]]
    """
    a = np.arange(6).reshape(2, 3)  # [[0,1,2],[3,4,5]]
    b = np.arange(10, 40, 10)  # [10,20,30]
    print(a)
    print(b)
    print(a + b)

    # 数组也可以与数字做运算
    # [[0,1,2],[3,4,5]] * 2 = [[0,1,2],[3,4,5]] * [[2,2,2],[2,2,2]] = [[0,2,4],[6,8,10]]
    print(a * 2)

    # 维度从尾开始匹配，如果发现不一致，比如a.shape=(2,3),b.shape=(2,2)，两者运算会报错
    b = np.arange(4).reshape(2, 2)
    # print(a+b)  # 报错

    # 对于不同形状的数组，如果其中一个从尾开始是1，则也能进行运算，运算后的形状为较大数组的形状
    a = a.reshape(2, 3)
    b = np.ones(4).reshape((2, 2, 1))
    print(a)
    print(b)
    print(a+b)
    print((a+b).shape)  # (2, 2, 3)
    print(a*b)

    # 如果两个数组轴的数量相等, 则运算后的形状依然为较大数组的形状
    a = np.arange(12).reshape((2, 2, 3))
    b = np.ones(4).reshape((2, 2, 1))
    print(a)
    print(b)
    print(a+b)
    print((a + b).shape)  # (2, 2, 3)

    a = np.arange(6).reshape(1, 6)
    b = np.arange(4).reshape((2, 2))
    print("a + b无法运算")

    # 但只要在b上增加一个数据宽度为1的维度，则可以运算
    a = np.arange(6).reshape(1, 6)
    b = np.arange(4).reshape((2, 2, 1))
    print(a)
    print(b)
    print("结果")
    print(a+b)

    # b也可以通过np.newaxis这种方式增加维度,但不增加在最后一个维度，而是第二个维度
    print("使用np.newaxis")
    b = np.arange(4).reshape((2, 2))
    b = b[:, np.newaxis]
    print(b.shape)
    print(b)
    # print("a+b")
    # print(a+b)

    print("相同维度数组运算")
    a = np.arange(4).reshape(2, 2)
    b = np.arange(4).reshape(2, 2)
    print(a)
    print(b)
    print(a + b)





