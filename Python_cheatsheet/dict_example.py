#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/12 21:24
@Author  : luocai
@file    : dict_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

字典知识点
"""
# 创建字典 3 种方式
# {} 形式
dic1 = {'name': 'python', 'age': 20}
# 内置方法 dict()
dic2 = dict(name='p', age=3)
# 字典推导式
dic3 = {x: x ** 2 for x in {2, 4, 6}}
print('dic1={}'.format(dic1))
print('dic2={}'.format(dic2))
print('dic3={}'.format(dic3))

# 三个常见的内置方法,keys(), values(), items()
print('keys()方法，dic1.keys()={}'.format(dic1.keys()))
print('values()方法, dic1.values()={}'.format(dic1.values()))
print('items()方法, dic1.items()={}'.format(dic1.items()))

# 修改和访问
dic1['age'] = 33
dic1.setdefault('sex', 'male')
print('dic1={}'.format(dic1))
# get() 访问某个键
print('dic1.get(\'age\', 11)={}'.format(dic1.get('age', 11)))
print('访问某个不存在的键，dic1.get(\'score\', 100)={}'.format(dic1.get('score', 100)))
# 删除
del dic1['sex']
print('del dic1[\'sex\'], dic1={}'.format(dic1))
dic1.pop('age')
print('dic1.pop(\'age\'), dic1={}'.format(dic1))
# 清空
dic1.clear()
print('dic1.clear(), dic1={}'.format(dic1))
# 合并两个字典
print('合并 dic2 和 dic3 前, dic2={}, dic3={}'.format(dic2, dic3))
dic2.update(dic3)
print('合并后，dic2={}'.format(dic2))

# 遍历字典
dic4 = {'a': 1, 'b': 2}
for key, val in dic4.items():
    print('{}: {}'.format(key, val))
# 不需要采用 keys()
for key in dic4:
    print('{}: {}'.format(key, dic4[key]))

# 判断数据类型是否不可改变
# id() 方法
i = 2
print('i id value=', id(i))
i += 3
print('i id value=', id(i))

l1 = [1, 3]
print('l1 id value=', id(l1))
l1.append(4)
print('l1 id value=', id(l1))

# hash
s = 'abc'
print('s hash value: ', hash(s))
l2 = ['321', 1]
print('l2 hash value: ', hash(l2))

