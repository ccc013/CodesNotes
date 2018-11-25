#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
阶跃函数的简单实现
"""
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    '''
    阶跃函数
    :param x:
    :return:
    '''
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    '''
    sigmoid 激活函数
    :param x:
    :return:
    '''
    return 1 / (1 + np.exp(-x))


def relu(x):
    '''
    ReLU 激活函数
    :param x:
    :return:
    '''
    return np.maximum(0, x)


def activation_function_show(func_name):
    # 简单生成一个范围是 -5.0 到 5.0，步长是 0.1 的 Numpy 数组, 总共 100 个数
    x = np.arange(-5.0, 5.0, 0.1)
    if func_name == 'step':
        y = step_function(x)
    elif func_name == 'sigmoid':
        y = sigmoid(x)
    elif func_name == 'relu':
        y = relu(x)
    else:
        raise ValueError('Invalid Function name!')
    # 画图展示阶跃函数
    plt.plot(x, y)
    # 指定 y 轴的范围
    if not func_name == 'relu':
        plt.ylim(-0.1, 1.1)
    plt.show()


def sig_step_compare():
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = step_function(x)
    y2 = sigmoid(x)
    plt.plot(x, y1)
    # 指定采用 sigmoid 函数图形的颜色和线类型分别是 红色和虚线
    plt.plot(x, y2, 'r--')
    plt.ylim(-0.1, 1.1)
    plt.show()


if __name__ == '__main__':
    func_names = ['step', 'sigmoid', 'relu']
    activation_function_show(func_names[2])
    # sig_step_compare()
