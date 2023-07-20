# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    str = "this is the way"
    # 字符串索引
    print str[0]

    # 对于中文，一个中文字符等于3个英文字符
    str = "这是一个中文字符串"
    # 打印‘这’字
    print str[:3]

    # 字符串截取，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的
    # 索引'2'可以理解为字符串从左往右数第2个
    str = "this is the way"
    print str[:2]

    # 原始字符串。 没有特殊字符或不能打印的字符
    print r"\\n%s"

    # 将字符串首字母大写
    print "abc".capitalize()

    # 字符串全大写/小写
    print "ABC".upper()
    print "abc".lower()

    # 判断字符串是否以指定字符串结尾或开始
    print "abc".endswith("bc")
    print "abc".startswith("ab")

    # 指定字符串作为分隔符，将可序列的对象(list,array,字符串等)合并成一个新的字符串
    print ",".join(['1', '2', '3', '4'])
    print ",".join('1234')

    # 清楚左右两边的空格
    print " a b c ".strip()

    # 以指定分隔符截取字符串，函数参数为指定分隔符，返回一个list
    print "a,b,c,d".split(",")
