#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/14 23:12
@Author  : cai

模型的性能度量，二分类
"""


def accuracy(y_true, y_pred):
    return sum(y == y_p for y, y_p in zip(y_true, y_pred)) / len(y_true)


def error(y_true, y_pred):
    return sum(y != y_p for y, y_p in zip(y_true, y_pred)) / len(y_true)


def precision(y_true, y_pred):
    true_positive = sum(y and y_p for y, y_p in zip(y_true, y_pred))
    predicted_positive = sum(y_pred)
    return true_positive / predicted_positive


def recall(y_true, y_pred):
    true_positive = sum(y and y_p for y, y_p in zip(y_true, y_pred))
    real_positive = sum(y_true)
    return true_positive / real_positive


def true_negative_rate(y_true, y_pred):
    true_negative = sum(1 - (yi or yi_hat) for yi, yi_hat in zip(y_true, y_pred))
    actual_negative = len(y_true) - sum(y_true)
    return true_negative / actual_negative


def roc(y, y_hat_prob):
    thresholds = sorted(set(y_hat_prob), reverse=True)
    ret = [[0, 0]]
    for threshold in thresholds:
        y_hat = [int(yi_hat_prob >= threshold) for yi_hat_prob in y_hat_prob]
        ret.append([recall(y, y_hat), 1 - true_negative_rate(y, y_hat)])
    return ret


def get_auc(y, y_hat_prob):
    roc_val = iter(roc(y, y_hat_prob))
    tpr_pre, fpr_pre = next(roc_val)
    auc = 0
    for tpr, fpr in roc_val:
        auc += (tpr + tpr_pre) * (fpr - fpr_pre) / 2
        tpr_pre = tpr
        fpr_pre = fpr
    return auc


if __name__ == '__main__':
    y_true = [1, 0, 1, 0, 1]
    y_pred = [0, 0, 1, 1, 0]
    y_hat_prob = [0.9, 0.85, 0.8, 0.7, 0.6]

    acc = accuracy(y_true, y_pred)
    err = error(y_true, y_pred)
    precisions = precision(y_true, y_pred)
    recalls = recall(y_true, y_pred)
    print('accuracy=', acc)
    print('error=', err)
    print('precisions=', precisions)
    print('recalls=', recalls)

    roc_list = roc(y_true, y_hat_prob)
    auc_val = get_auc(y_true, y_hat_prob)
    print('roc_list:', roc_list)
    print('auc_val:', auc_val)
