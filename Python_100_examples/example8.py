#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/27 21:36
@Author  : cai

example 8 come from http://www.runoob.com/python/python-exercise-example8.html
example 9 come from http://www.runoob.com/python/python-exercise-example9.html

"""
import time


# ============== Example 8 ======================================
# 乘法口诀
# ===============================================================

# 第一种，for 循环实现
def multiplication_table1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%-2d ' % (i, j, i * j), end='')
        print('')


# 第二种，一行代码实现
def multiplication_table2():
    print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))


# ============== Example 9 ======================================
# 暂停一秒输出
# ===============================================================

def sleep_print():
    print("Start : %s" % time.ctime())
    time.sleep(1)
    print("End : %s" % time.ctime())


# ============== Example 10 ======================================
# 暂停一秒输出，然后格式化当前时间
# ===============================================================

def sleep_print2():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

if __name__ == '__main__':
    # multiplication_table1()
    # multiplication_table2()
    # sleep_print()
    # sleep_print2()

    print('finish')
