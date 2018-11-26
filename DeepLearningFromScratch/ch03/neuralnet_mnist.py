#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
inference with a simple neural network and use mnist dataset
"""
import sys, os

sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import numpy as np
import pickle
from common.functions import sigmoid, softmax
import time


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, label = get_data()
network = init_network()

accuracy_cnt = 0
start_time = time.time()
for i in range(len(x)):
    y = predict(network, x[i])
    # 获取概率最高的元素的索引, 也就是输出类别
    idx = np.argmax(y)
    if idx == label[i]:
        accuracy_cnt += 1
# total time:  0.4882946014404297
print('total time: ', time.time() - start_time)
# Accuracy: 0.9352
print('Accuracy: ' + str(float(accuracy_cnt) / len(x)))
