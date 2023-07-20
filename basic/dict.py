# coding=utf-8
if __name__ == '__main__':
    # 创建字典,字典值可以是任意对象
    # 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    # 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
    dt = {"b": "b"}

    # 增加元素
    dt["a"] = "a"
    print dt

    # 删除元素
    del dt["a"]

    # 修改元素，与增加一样
    dt["b"] = "a"
    print dt

    # 更新多个键值对
    u_dt = {"c": "c", "b": "b"}
    dt.update(u_dt)
    print dt

    # 查询
    print "b" in dt

    # 遍历
    for k in dt:
        print "key=%s,value=%s" % (k, dt[k])

    # 清空
    dt.clear()
    print dt
