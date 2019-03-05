#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/27 21:36
@Author  : cai

example 8 come from http://www.runoob.com/python/python-exercise-example8.html
"""


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


if __name__ == '__main__':
    multiplication_table1()
    multiplication_table2()
    print('finish')
