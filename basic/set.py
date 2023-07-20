# coding=utf-8
if __name__ == '__main__':
    # 集合（set）是一个无序的不重复元素序列。
    # 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
    # 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。

    # 创建一个空集合，必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
    st = set()

    # 创建一个非空集合
    st = {1, 2, 3, 4, 5}

    # 增
    st.add(6)
    print st

    # 删,如果元素不存在，则会发生错误
    st.remove(6)
    print st

    # 删除，如果元素不存在，不会报错
    st.discard(6)

    # 两个集合的差集, set([1, 2, 5])
    st2 = {3, 4}
    print st.difference(st2)

    # 两个集合的交集,set([3, 4])
    print st.intersection(st2)

    # 判断两个集合是否有相同的元素，如果没有返回 True，否则返回 False。
    # False
    print st.isdisjoint(st2)

    # 判断指定集合是否为参数集合的子集,true
    print st2.issubset(st)

    # 判断参数集合是否为指定集合的子集，true
    print st.issuperset(st2)
