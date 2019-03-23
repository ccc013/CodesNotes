#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/17 13:58
@Author  : cai

如何实现字符串常量转变量，相当于动态生成变量
"""


lists = ['A', 'B', 'C', 'D']

# 解法1，利用 globals() 修改全局变量空间

for i in lists:
    globals()[i] = []

# 打印 []
print(A)

# 解法2，利用 exce()
for i in lists:
    # python3.6 的实现
    # exec(f"{i}=[]")
    # exec('{} = [1]'.format(i))
    # exec(i +'=[2]')
    exec(' '.join([i, '=[3]']))

print(B)

