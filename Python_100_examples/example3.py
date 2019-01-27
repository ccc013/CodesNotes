#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/26 22:29
@Author  : cai

examples come from http://www.runoob.com/python/python-exercise-example3.html
"""


# ============== Example 3 ======================================
#  一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# ===============================================================

def perfect_square():
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i;
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x)


def perfect_square2():
    '''
    列表推导式
    :return:
    '''
    [print(m ** 2 - 100, end=',') for m in range(1, 169) for n in range(1, 169) if (n ** 2 - m ** 2) == 168]


def perfect_square2_loop():
    '''
    for 循环形式
    :return:
    '''
    for m in range(1, 169):
        for n in range(1, 169):
            if (n ** 2 - m ** 2) == 168:
                print(m ** 2 - 100, end=',')


if __name__ == '__main__':
    perfect_square()
    perfect_square2()
    print('\n')
    perfect_square2_loop()
