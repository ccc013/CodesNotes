#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/16 20:36
@Author  : cai

example 6 come from http://www.runoob.com/python/python-exercise-example6.html
example 7 come from http://www.runoob.com/python/python-exercise-example7.html
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


# ============== Example 7 ======================================
# 复制列表
# ===============================================================

def copy_list(input_list):
    print('original list: {}'.format(input_list))
    copyed_list = input_list[:]
    print('copyed_list: {}'.format(copyed_list))


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

    list1 = [3, 2, '1', [1,2]]
    copy_list(list1)

    print('finish!')
