#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/13 16:25
@Author  : luocai
@file    : set_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

集合
"""
# 创建集合
s1 = {'a', 'b', 'c'}
s2 = set()
s3 = set('abc')
print('s1={}'.format(s1))
print('s2={}'.format(s2))
print('s3={}'.format(s3))

# 删除重复元素
s4 = set('good')
print('s4={}'.format(s4))

# 增加元素，add() 和 update()
s1.add('dd')
print('s1.add(\'dd\'), s1={}'.format(s1))
s1.update('o')
print('添加一个元素，s1={}'.format(s1))
s1.update(['n', 1])
print('添加多个元素, s1={}'.format(s1))
s1.update([12, 33], {'ab', 'cd'})
print('添加列表和集合, s1={}'.format(s1))

# 删除元素, pop(), remove(), clear()
print('s3={}'.format(s3))
s3.pop()
print('随机删除元素, s3={}'.format(s3))
s3.clear()
print('清空所有元素, s3={}'.format(s3))
s1.remove('a')
print('删除指定元素,s1={}'.format(s1))

# 判断是否子集, issubset()
a = set('abc')
b = set('bc')
c = set('cd')
print('b是否a的子集:', b.issubset(a))
print('c是否a的子集:', c.issubset(a))

# 并集操作，union() 或者 |
print('a 和 c 的并集:', a.union(c))
print('a 和 c 的并集:', a | c)

# 交集操作，intersection() 或者 &
print('a 和 c 的交集:', a.intersection(c))
print('a 和 c 的交集:', a & c)

# 差集操作，difference() 或者 -，即只存在一个集合的元素
print('只在a中的元素:', a.difference(c))
print('只在a中的元素:', a - c)

# 对称差集, symmetric_difference() 或者 ^, 求取只存在其中一个集合的所有元素
print('对称差集:', a.symmetric_difference(c))
print('对称差集:', a ^ c)
