#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/16 20:18
@Author  : cai

example come from http://www.runoob.com/python/python-exercise-example5.html
"""


# ============== Example 5 ======================================
#  输入三个整数 x,y,z，请把这三个数由小到大输出。
# ===============================================================

def sort_numbers_1():
    x = int(input('integer:\n'))
    y = int(input('integer:\n'))
    z = int(input('integer:\n'))
    print('input numbers: x=%d, y=%d, z=%d' % (x, y, z))
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    print('sorted: x=%d, y=%d, z=%d' % (x, y, z))

# 利用列表的内置函数 sort()
def sort_numbers_2():
    l = []
    for i in range(3):
        x = int(input('integer:\n'))
        l.append(x)
    print('original list:', l)
    l.sort()
    print('sorted:', l)


if __name__ == '__main__':
    sort_numbers_1()
    sort_numbers_2()
    print('finish!')
