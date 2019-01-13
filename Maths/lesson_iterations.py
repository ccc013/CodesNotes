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
    for i in range(2, grid + 1):
        wheat_numbers *= 2
        sums += wheat_numbers

    print('when grid = %d, wheats numbers = %d' % (grid, sums))

    return sums


def get_square_root(n, threshold, max_try):
    '''
    计算大于 1 的正整数的平方根
    :param n: 给定正整数
    :param threshold: 误差的阈值
    :param max_try: 最大尝试次数
    :return:
    '''
    if n <= 1:
        return -1.0
    # interval boundary 区间的左右边界
    left = 1.0
    right = float(n)
    for idx in range(max_try):
        # 防止溢出
        middle = left + (right - left) / 2
        square = middle * middle
        # 误差
        delta = abs(square / n - 1)
        if delta <= threshold:
            return middle
        else:
            if square > n:
                right = middle
            else:
                left = middle

    return -2.0


def search_word(dictionary, word):
    '''
    查找匹配单词
    :param dictionary: 排序后的字典
    :param word:待查找单词
    :return:
    '''
    if dictionary is None:
        return False
    if len(dictionary) < 1:
        return False

    left = 0
    right = len(dictionary) - 1
    while left <= right:
        middle = int(left + (right - left) / 2)
        if dictionary[middle] == word:
            return True
        else:
            if dictionary[middle] > word:
                right = middle - 1
            else:
                left = middle + 1

    return False


if __name__ == '__main__':
    # print('compute numbers of wheat!')
    # numbers_grid = 63
    # get_number_of_wheat(numbers_grid)

    # print('get square root')
    # square_root = get_square_root(10, 0.000001, 10000)
    # if square_root == -1.0:
    #     print('please input a number > 1')
    # elif square_root == -2.0:
    #     print('cannot find the square root')
    # else:
    #     print('square root==', square_root)

    print('find word in dictionary')
    dict_list = ['i', 'am', 'coder']
    dict_list = sorted(dict_list)
    print('sorted dict:', dict_list)
    word_to_find = 'am'
    found = search_word(dict_list, word_to_find)
    if found:
        print('word "%s" found in dictionary--%s!' % (word_to_find, dict_list))
    else:
        print('cannot find the word "%s"' % word_to_find)

    print('finish')
