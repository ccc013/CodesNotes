#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/16 20:36
@Author  : cai

example come from http://www.runoob.com/python/python-exercise-example6.html
"""
import time


# ============== Example 6 ======================================
# 斐波那契数列
# ===============================================================

# 采用迭代循环实现
def fib1(n):
    a, b = 1, 1
    # n 必须大于等于 2
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 递归实现
def fib2(n):
    if 0 < n <= 2:
        return 1
    else:
        return fib2(n - 1) + fib2(n - 2)


# 输出指定个数的斐波那契数列
def fib_array(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == '__main__':
    start = time.time()
    a1 = fib1(30)
    print('fib1 cost time: ', time.time() - start)
    print('fib1 result=', a1)
    start2 = time.time()
    a2 = fib2(30)
    print('fib2 cost time: ', time.time() - start2)
    fibs = fib_array(10)
    print('fib2 result=', a2)
    print('fib array=', fibs)
    print('finish!')
