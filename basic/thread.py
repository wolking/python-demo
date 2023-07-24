# coding=utf-8
# !/usr/bin/python3
import threading
import time
import asyncio


def thread_func():
    """
    使用线程执行目标函数
    :return:
    """
    def target_func(i):
        for c in range(10):
            time.sleep(1)
            print "我在执行%d" % c
    args = (1,)
    th = threading.Thread(target=target_func, args=args)
    th.start()
    th.join()


if __name__ == '__main__':
    # 线程
    thread_func()

