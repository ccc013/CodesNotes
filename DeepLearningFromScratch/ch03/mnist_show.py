#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
show mnist dataset
"""
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import numpy as np
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 输出各个数据的形状
print(x_train.shape)  # (60000, 784)
print(t_train.shape)  # (60000,)
print(x_test.shape)  # (10000, 784)
print(t_test.shape)  # (10000)

img = x_train[0]
label = t_train[0]
print('label=', label)  # 5
# image shape: (784,)
print('image shape:', img.shape)
# 将图像形状调整回原来的形状
img = img.reshape(28, 28)
# after reshape, image shape: (28, 28)
print('after reshape, image shape:', img.shape)
img_show(img)
