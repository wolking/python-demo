import numpy as np

if __name__ == '__main__':
    # 花式索引，提供比常规python序列更多的索引功能

    """
    1、选择特定的元素：可以使用花式索引选择数组中指定位置的元素。
    通过提供索引数组或索引列表，可以轻松地选择数组中的特定元素。
    这种方法对于非连续的选择或对多维数组的选择特别有用。
    """

    print("场景1")
    a = np.array([[1, 2], [3, 4], [5, 6]])
    i_b = np.array([0, 2])  # 选中a索引为0和2的元素
    # [[1 2] [5 6]]
    print(a[i_b])

    # [[[1 2]] [[3 4]]]
    # 不难看出，其实就相当于取目标数组a指定索引的元素，放入索引数组对应位置
    # [[0], [1]] = [[a[0]], [a[1]]]
    i_b = np.array([[0], [1]])
    print(a[i_b])
    """
    2、按特定顺序重排数组：花式索引还可以用于按照指定的顺序重排数组中的元素。
    通过提供特定的索引顺序，可以重新排列数组的元素，从而改变它们的相对位置。
    """

    print("场景2")
    a = np.array([9, 2, 8, 4, 19])
    # 将数组从大到小排序
    i_b = np.array([4, 0, 2, 3, 1])
    print(a[i_b])

    """
    3、布尔索引，根据条件选择元素，但索引数组的轴的值必须与目标数组的任意一个轴的值一致
    """

    print("场景3")
    a = np.array([1, 2, 3, 4, 5])
    # i_b的轴必须与a一致，为5，不一致会报不匹配的错误
    i_b = np.array([True, False, True, False, False])
    print(a[i_b])

    """
    4、修改数组元素值
    """

    print("场景4")
    a = np.arange(6)
    print(a)
    # 修改第2与4个元素
    i_b = np.array([1, 3])
    a[i_b] = 10
    print(a)
    print("修改多维数组")
    a = a.reshape(3, 2)
    i_b = np.array([1, 2])
    print(a[i_b])
    # 如果索引所对应的元素是数组，通过一下方式修改值，会将该数组的所有元素修改为99
    # 索引1、2的元素被修改为[99,99]
    a[i_b] = 99
    print(a)   # [[ 0 10] [99 99] [99 99]]

    """
    5、多维数组索引操作与np.ix_()
    """

    print("场景5")
    # 普通数组索引，i_b取目标数组的行，i_c则是在这基础上找出对应列上的每一个元素
    # i_c取的是i_b中[第1行第2列，第2行第2列，第3行第3列]=[2 5 9]
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    i_b = np.array([0, 1, 2])
    i_c = np.array([1, 1, 2])
    print(a[i_b, i_c])

    # 使用np.ix_()，则在经过i_b得到的数组上，将i_c的每一个元素作为索引，对每一行取出对应的元素
    i_d = np.ix_(i_b, i_c)
    # i_d是一个元组，第一个元素是[[0],[1],[2]],第二个元素为[[1, 1, 2]]
    print(i_d)
    # a[i_d]= [[2 2 3] [5 5 6] [8 8 9]]
    print(a[i_d])