# coding=utf-8


class CA:

    def __init__(self, a):
        self.a = a


def generator():
    """
    通过使用yield实现一个惰性迭代器
    :return:
    """
    i = 0
    while True:
        yield CA(i)
        i += 1
        if i > 10:
            raise StopIteration


if __name__ == '__main__':
    # 生成器
    g = generator()
    for ca in g:
        print ca.a
    c = next(g)  # 再次调用会报错
    print c.a


"""
yield的生成器与迭代器一样存在相同的优缺点，是迭代器的一种
应用场景：适合于处理大数据量和耗时操作的场景，
        例如遍历文件或网络数据流、CPU密集型计算、图像处理等。生成器可以逐个读取大文件，并且不必将整个文件加载到内存中，
        避免了内存消耗和IO操作的额外开销。

"""