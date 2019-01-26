#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/26 16:45
@Author  : cai

examples come from http://www.runoob.com/python/python-exercise-example1.html
"""


# ============== Example 1 ======================================
#  有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# ===============================================================

def create_three_digits(number_start=1, number_end=4):
    '''
    给定指定数字范围（比如1到4），求可以组成多少个无重复的三位数
    :param number_start: 起始数字
    :param number_end: 结束数字
    :return: 返回数量，以及可能的三位数的列表
    '''
    count = 0
    result_list = list()
    for i in range(number_start, number_end + 1):
        for j in range(number_start, number_end + 1):
            for k in range(number_start, number_end + 1):
                if (i != j) and (i != k) and (j != k):
                    count += 1
                    result_list.append(str(i) + str(j) + str(k))
    return count, result_list


def create_three_digits2(number_start=1, number_end=4):
    '''
    采用列表推导式实现
    :param number_start:
    :param number_end:
    :return:
    '''
    return [str(i) + str(j) + str(k) for i in range(number_start, number_end + 1) for j in
            range(number_start, number_end + 1) for k in
            range(number_start, number_end + 1) if (i != j) and (i != k) and (j != k)]


if __name__ == '__main__':
    count, result_list = create_three_digits(number_start=1, number_end=4)
    print('valid count={}, and they are:'.format(count))
    for result in result_list:
        print(result)

    result2 = create_three_digits2(number_start=1, number_end=4)
    print('numbers:', len(result2))
    for result in result2:
        print(''.join(str(result[:])))
