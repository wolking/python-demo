# coding=utf-8

def catch_err(i):
    """
    捕获异常，异常处理
    :param i:
    :return:
    """
    try:
        """执行代码"""
        print "执行代码"
        if i > 0:
            raise IOError("这是一个错误")
    except IOError as err:
        """发生异常时执行的代码"""
        # print "发生异常时执行的代码"
        print "捕获到异常，err_msg="+err.message
    else:
        """没有异常时执行的代码"""
        # print "没有异常时执行的代码"
        print "没有异常"
    finally:
        """不管有没有异常都会执行的代码"""
        # print "不管有没有异常都会执行的代码"
        print "结束"


if __name__ == '__main__':
    # 捕获异常，异常处理
    catch_err(0)
    print ""
    catch_err(1)
