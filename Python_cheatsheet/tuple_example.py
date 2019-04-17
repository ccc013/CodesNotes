#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/25 23:56
@Author  : cai

元组知识点
"""
# ===============================================================
# 初始化
# ===============================================================
# 创建空元祖，两种方法
t1 = tuple()
t2 = ()
t3 = (1, 2, '2', [1, 2], 5)
# 创建一个元素的元祖
t4 = (7,)
t5 = (2)
print('创建两个空元组：t1={}, t2={}'.format(t1, t2))
print('包含不同元素类型的元组：t3={}'.format(t3))
print('包含一个元素的元祖: t4=(7, )={}, t5=(2)={}'.format(t4, t5))
print('type(t4)={}, type(t5)={}'.format(type(t4), type(t5)))
print('输出元组的第一个元素：{}'.format(t3[0]))
print('输出元组的第二个到第四个元素：{}'.format(t3[1:4]))
print('输出元祖的最后一个元素: {}'.format(t3[-1]))
print('输出元祖两次: {}'.format(t3 * 2))
print('连接元祖: {}'.format(t3 + t4))

# 创建一个二维元组
tups = (1, 3, 4), ('1', 'abc')
print('二维元组: {}'.format(tups))


def print_tup():
    return 1, '2'


res = print_tup()
print('type(res)={}, res={}'.format(type(res), res))

# 元组不可修改，但如果元素可修改，那可以修改该元素内容
tup11 = (1, [1, 3], '2')
print('tup1={}'.format(tup11))
tup11[1].append('123')
print('修改tup11[1]后，tup11={}'.format(tup11))

# count()
print('tup11.count(1)={}'.format(tup11.count(1)))
# index()
print('tup11.index(\'2\')={}'.format(tup11.index('2')))
