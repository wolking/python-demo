# coding=utf-8
"""
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问
"""

# 该变量虽然拥有全局作用域，但无法在函数内使用
except_v = 1


def change_v():
    # 此处访问函数外定义的except_v，会报错，提示未定义
    # print except_v

    except_v = 10
    print except_v


def local():
    """
    变量的作用域
    :return:
    """
    if True:
        a = 1
    # 能访问到a
    print a
    for i in range(10):
        b = i
    # 也能访问到b
    print b

    try:
        c = 2
    except Exception:
        print "异常"

    # 访问到C
    print c


def global_v():
    """
    全局变量，使用关键字global设置变量为全局变量

    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
    :return:
    """
    global d
    d = 10


if __name__ == '__main__':
    # 作用域
    # local()

    # 全局变量
    # global_v()
    # print d

    change_v()
    print except_v
