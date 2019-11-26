#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/11/26 8:15 下午
@Author  : luocai
@file    : data_norm.py
@concat  : 429546420@qq.com
@site    :
@software: PyCharm Community Edition
@desc    :

数据标准化
"""

import math
import numpy as np


class DataNorm(object):

    def __init__(self):
        # sample
        self.arr = [i for i in range(1, 10)]
        # 最大值
        self.x_max = max(self.arr)
        # 最小值
        self.x_min = min(self.arr)
        # 平均值
        self.x_mean = sum(self.arr) / len(self.arr)
        # 标准差
        self.x_std = np.std(self.arr)

    # min-max 标准化
    def min_max(self):
        arr_ = list()
        for x in self.arr:
            # round(x, 4) 对 x 保留四位小数
            arr_.append(round((x - self.x_min) / (self.x_max - self.x_min), 4))
        print(f'after min-max norm: {arr_}')

    # Z-score 标准化
    def z_score(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x - self.x_mean) / self.x_std, 4))
        print(f'after z-score norm: {arr_}')

    # 小数定标标准化
    def decimal_scaling(self):
        arr_ = list()
        j = self.x_max // 10 if self.x_max % 10 == 0 else self.x_max // 10 + 1
        for x in self.arr:
            arr_.append(round(x / math.pow(10, j), 4))
        print(f'after decimal_scaling norm: {arr_}')

    # 均值归一化
    def mean_norm(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x - self.x_mean) / (self.x_max - self.x_min), 4))
        print(f'after mean norm: {arr_}')

    # 向量标准化
    def vector_norm(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round(x / sum(self.arr), 4))
        print(f'after vector norm: {arr_}')

    # 指数转换法
    def exponential(self):
        arr_1 = list()
        for x in self.arr:
            arr_1.append(round(math.log10(x) / math.log10(self.x_max), 4))
        print(f'after exponential(log10) norm: {arr_1}')

        arr_2 = list()
        sum_e = sum([math.exp(one) for one in self.arr])
        for x in self.arr:
            arr_2.append(round(math.exp(x) / sum_e, 4))
        print(f'after exponential(softmax) norm: {arr_2}')

        arr_3 = list()
        for x in self.arr:
            arr_3.append(round(1 / (1 + math.exp(-x)), 4))
        print(f'after exponential(sigmoid) norm: {arr_3}')


if __name__ == '__main__':
    dn = DataNorm()
    dn.min_max()
    dn.z_score()
    dn.decimal_scaling()
    dn.mean_norm()
    dn.vector_norm()
    dn.exponential()
