#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""

"""
import numpy as np
import sys, os

# 为了导入父目录的文件而进行的设定
sys.path.append(os.pardir)
from common.functions import sigmoid, identity_function, softmax


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forword(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forword(network, x)
    # y= [0.31682708 0.69627909]
    print('y=', y)
    y_softmax = softmax(y)
    # softmax= [0.40625907 0.59374093]
    print('softmax=', y_softmax)
