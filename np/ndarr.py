# coding=utf-8
import numpy as np

if __name__ == '__main__':
    # N维数组
    """
    array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
    
    p_object: 数组或list或元组等可迭代的对象
    dtype: 数组元素的数据类型，可选，可将每一个数字元素在int与str间互转
    copy: 对象是否需要复制，可选
    subok:返回一个与基类类型一致的数组
    ndmin:
    
    """
    arr = np.array([1, 2, 3, 4])
    print arr

    tupleArr = np.array((1, 2))
    print tupleArr

    # 无法将无序不重复集合转数组
    setArr = np.array({1, 2, 3, 4, 5})
    print setArr

    # 不能将字典转数组
    dicArr = np.array({"k1": 1, "k2": 2})
    print dicArr

    # 直接将数组元素int转成str
    arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=str)
    print arr

    # 直接将数组元素str转int
    arr = np.array(['1', '2'], dtype=int)
    print arr

    # 无法转换
    # arr = np.array(['a', 'b'], dtype=int)
    # print arr

    lt = [[1, 2, 3]]
    print id(lt[0])
    arr = np.array(lt, copy=True)
    print id(arr[0])
    print arr.ndim

    # subok
    nlt = np.array(lt, subok=True)
    print nlt

    lt = np.array([1, 2, 3])
    lt2 = np.array([4, 5, 6])
    print lt * lt2

