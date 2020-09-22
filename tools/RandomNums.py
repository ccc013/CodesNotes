#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/22 9:56 上午
@Author  : luocai
@file    : RandomNums.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

随机数生成器，输入随机抽取的数量范围 N，返回序号（1-N）
"""
import random


def random_choose_num(n):
    '''
    输入数量范围 n, 返回随机选择的序号
    :param n: 大于 0的整数
    :return:
    '''
    return random.randint(1, n)


def main():
    while True:
        try:
            n = input('请输入随机抽取的总数：(输入q退出)')
            if n == 'q':
                print('随机抽取结束')
                exit()
            n = int(n)
            res = random_choose_num(n)
            print(f"随机选择的序号为: {res}")
        except Exception as err:
            print('请输入一个整数')


if __name__ == '__main__':
    main()
