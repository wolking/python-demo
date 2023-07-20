#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A:
    """
    类A
    """


class B(A):
    """
    类B，继承A
    """


def get_type(v):
    """
    获取变量类型，获取的是直接类型，无法获取父类
    :return:
    """
    ty = type(v)
    print(ty)

    # 类
    b = B()
    print(type(b) == A)  # False


def is_instance_int(v):
    """
    判断变量是否是指定int类型，能判断是否继承父类
    :param v:
    :return:
    """
    # 基本类型
    is_int = isinstance(v, int)
    print(is_int)

    # 类
    b = B()
    print(isinstance(b, B))  # True
    print(isinstance(b, A))  # True


def reverse_str(str):
    """
    翻转字符串
    :param str:
    :return:
    """
    print("旧的字符串: ", str)
    words = list(str)
    words = words[-1::-1]
    new_word = "".join(words)
    print("新的字符串：", new_word)


def iterate_dict(dict):
    """
    遍历字典类型
    :param dict:
    :return:
    """
    for k in dict.keys():
        print("key=", k, "value=", dict[k])

    for k, v in dict:
        print("key=", k, "value=", v)

    for v in dict.values():
        print("value=", v)


def logical_operator():
    """
    逻辑运算符,优先级not>and>or
    :return:
    """
    a = True
    b = False
    print("a = ", a, "b = ", b)
    print("a and b:", a and b)
    print("a or b:", a or b)
    print("not a:", not a)
    print("not b:", not b)


if __name__ == '__main__':
    # get_type(1)
    # is_instance_int(2)
    # reverse_str("张洁升Jason")
    # iterate_dict({"k1": 1, "k2": 2, "k3": 3})
    logical_operator()

# python不支持Switch语句，没有do...while循环
# pass语句用于占位，因为如果定义一个空函数，程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。