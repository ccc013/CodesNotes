#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/12 18:01
@Author  : cai

迭代法
"""


def get_number_of_wheat(grid):
    '''
    \计算放到给定格子数量需要的麦子数量
    :param grid: 格子数
    :return:
    '''
    # f(1) = 1
    wheat_numbers = 1

    sums = wheat_numbers
    for i in range(2, grid+1):
        wheat_numbers *= 2
        sums += wheat_numbers

    print('when grid = %d, wheats numbers = %d' % (grid, sums))

    return sums


if __name__ == '__main__':
    print('compute numbers of wheat!')
    numbers_grid = 63
    get_number_of_wheat(numbers_grid)
    print('finish')
