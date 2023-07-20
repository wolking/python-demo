# coding=utf-8

class MyClass:
    """
    自定义类
    """

    # 基本属性,通过类名访问(MyClass.name),与实例变量重名,不会互相覆盖，可直接修改类属性值
    name = 'Jason'
    age = 10
    # 私有属性，类外部不可访问
    __weight = 20

    def __init__(self, name):
        """
        构造方法
        self:代表类的实例，而不是类，self并非关键字，只是惯例，约定第一个参数为实例，换成a/b/c都可以
                self.class指向类
        name:实例变量
        """
        self.name = name

    def my_func(self):
        """
        成员方法
        :return:
        """
        print "我是成员方法my_func"
        self.__private_func()

    def __private_func(self):
        print "私有方法"


class MyClassChild(MyClass):
    def __init__(self, name):
        # 调用父类的构造方法，可选
        # MyClass.__init__(self, name)
        print "aaaaa"

    def my_func(self):
        """
        重写父类方法
        :return:
        """
        print "我是子类MyClassChild重写父类的成员方法my_func"


class MyOperator:
    """
    类实现运算符自定义
    """

    def __init__(self, i):
        self.i = i
        print "初始化"

    def __len__(self):
        return 1 + self.i

    def __del__(self):
        # 类自我销毁最终也会执行该函数
        print "删除自己%d" % self.i

    def __add__(self, other):
        print "相加%d" % self.i

    def __sub__(self, other):
        print "相减%d" % self.i

    def __mul__(self, other):
        print "相乘%d" % self.i

    def __div__(self, other):
        print "相除%d" % self.i


def class_func():
    # 类
    print MyClass.name
    mc = MyClass("a")
    mc.my_func()
    print mc.name
    # 类属性不变
    print MyClass.name
    # 修改类属性值
    MyClass.name = "NewJason"
    print MyClass.name


def extend():
    # 继承
    mc = MyClassChild("子类")
    mc.my_func()


if __name__ == '__main__':
    # 类与继承
    class_func()
    extend()
    print ""
    o = MyOperator(1)
    print len(o)
    o2 = MyOperator(2)
    o + o2
    o * o2
    o / o2
    # del o
