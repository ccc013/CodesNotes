#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/23 23:09
@Author  : cai

practise for different loss function
"""
import numpy as np


def rmse(predictions, targets):
    # 真实值和预测值的误差
    differences = predictions - targets
    differences_squared = differences ** 2
    mean_of_differences_squared = differences_squared.mean()
    # 取平方根
    rmse_val = np.sqrt(mean_of_differences_squared)
    return rmse_val


def mae(predictions, targets):
    differences = predictions - targets
    absolute_differences = np.absolute(differences)
    mean_absolute_differences = absolute_differences.mean()
    return mean_absolute_differences


def mbe(predictions, targets):
    differences = predictions - targets
    mean_absolute_differences = differences.mean()
    return mean_absolute_differences


def loss_test():
    y_hat = np.array([0.000, 0.166, 0.333])
    y_true = np.array([0.000, 0.254, 0.998])

    print("d is: " + str(["%.8f" % elem for elem in y_hat]))
    print("p is: " + str(["%.8f" % elem for elem in y_true]))
    rmse_val = rmse(y_hat, y_true)
    print("rms error is: " + str(rmse_val))
    mae_val = mae(y_hat, y_true)
    print("mae error is: " + str(mae_val))

    mbe_val = mbe(y_hat, y_true)
    print("mbe error is: " + str(mbe_val))


if __name__ == '__main__':
    loss_test()
    print('finish!')
