# coding=utf-8

class MyIter:
    """
    自定义迭代器
    """

    def __init__(self):
        pass

    def __iter__(self):
        """
        自定义迭代器需实现该方法
        :return:
        """
        self.a = 0
        return self

    def __next__(self):
        """
        自定义迭代器需实现该方法,仅Python3支持，Python2中是next()
        :return:
        """
        self.a += 1
        return self.a

    def next(self):
        """
        仅python2支持
        问题：这里没有设置终止条件，外部的for循环将进行无限循环,使用StopIteration终止循环
        :return:
        """
        self.a += 1
        if self.a == 10:
            raise StopIteration
        return self.a

    def get_a(self):
        return self.a


if __name__ == '__main__':
    # 迭代器
    it = MyIter()
    for a in it:
        print a
        if a == 20:
            break
    print it.get_a()


"""
 - 优点：迭代器对象表示的是一个数据流，可以在需要时才去调用next来获取一个值；
         因而本身在内存中始终只保留一个值，对于内存占用小可以存放无限数据流。
         优于其他容器需要一次将所有元素都存放进内存，如：列表、集合、字典...等
 - 缺点：1.无法获取存放的元素长度，除非取完计数。
         2.取值不灵活，只能向后取值，next()永远返回的是下一个值；
         3.无法取出指定值(无法像字典的key,或列表的下标)，而且迭代器对象的生命周期是一次性的，元素被迭代完则生命周期结束。

"""