# coding=utf-8


def undefined_param_length(a, *args):
    """
    不定长参数，加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数，不需要指定参数名
    :param a:
    :param args: 参数个数不定，args为元组类型
    :return:
    """
    print args


def undefined_param_length2(**kwargs):
    """
    不定长参数，带两个*的参数会以字典的方式导入，但必须指定参数名
    :param kwargs: 字典类型
    :return:
    """
    print kwargs


def anonymous(d):
    a = lambda i: i+10
    b = lambda j, h, c: a(d)+j+h+c
    print b(1, 2, 3)


if __name__ == '__main__':
    # 函数
    # undefined_param_length(1, 2, 3, 4)
    # undefined_param_length2(a=1, b=2, c=3)
    anonymous(5)
