# coding=utf-8

def compare(x, y):
    """
    比较两个数的大小
    :param x:
    :param y:
    :return:
    """
    if x < y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


if __name__ == '__main__':
    # 创建一个有序列表list,列表元素类型可以相同，也可以不同
    lt = [1, 2, 3, 4, 5]

    # 获取list长度
    print len(lt)

    # 添加元素到末尾
    lt.append("6")
    print lt

    # 添加元素到指定索引位置，list.insert(index, obj)
    # [7, 1, 2, 3, 4, 5, '6']
    lt.insert(0, 7)
    print lt
    del lt[0]

    # 移除末尾元素，,[1, 2, 3, 4, 5]
    lt.pop()
    print lt

    # 删除指定元素,[2, 3, 4, 5]
    lt.remove(1)
    print lt

    # 删除指定索引的元素,[2, 3, 5]
    del lt[2]
    print lt

    # 修改指定索引的值,[1, 3, 5]
    lt[0] = 1
    print lt

    # 查询指定元素是否在list中,True
    print 1 in lt

    # 两个list相加,不会去重，返回一个新的list，旧的list不受影响。[1, 3, 5, 1, 3, 5]
    print lt + [1, 3, 5]
    print lt  # [1, 3, 5]

    # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表），[1, 3, 5, 2, 4, 6]
    lt.extend([2, 4, 6])
    print lt

    # 对list进行排序,cmp为比较函数，[6, 5, 4, 3, 2, 1]
    lt.sort(cmp=compare)
    print lt

    # list中最大的元素,6
    print max(lt)

    # list中最小的元素,1
    print min(lt)

    # 清空list, list.clear()只在Python3存在
    del lt[:]
    print lt
else:
    print "我来自list模块，只在导入时执行"

