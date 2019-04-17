#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/25 22:08
@Author  : cai
"""

# 缩进例子

# 正确示例
i = 2
if i == 3:
    print('true!')
else:
    print('False')

# 错误示例
if i == 3:
    print('i:')
    print(i)
else:
    print('wrong answer!')
    print('please check again')

sentence1 = "I love " + \
            "python"

sentence2 = ["I", "love",
             "python"]

print('Hello');
print('world')

# 等待用户输入
# user_input = input('请输入一个数字:\n')
# print('user_input=', user_input)

a = 3
b = 2
c = 4
d = 5
# 默认换行
print(a)
print(b)
# 不换行
print(c, end=',')
print(d)

# 变量赋值
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)
# 多个变量赋值
n = m = k = 2
cc, mm, nn = 1, 3.2, 'abc'
print('n=m=k=', n, m, k)
print('cc=', cc)
print('mm=', mm)
print('nn=', nn)

# int
q = 1
# float
w = 2.3
# bool
e = True
# complex
r = 1 + 3j
print(q, w, e, r)  # 1 2.3 True (1+3j)

# 内置的 type() 函数可以用来查询变量所指的对象类型
print(type(q))  # <class 'int'>
print(type(w))  # <class 'float'>
print(type(e))  # <class 'bool'>
print(type(r))  # <class 'complex'>

# 也可以采用 isinstance()
# isinstance 和 type 的区别在于：type()不会认为子类是一种父类类型，isinstance()会认为子类是一种父类类型
print(isinstance(q, int))  # True
print(isinstance(q, float))  # False

# 数值运算
# 加
print('2 + 3 =', 2 + 3)  # 2 + 3 = 5
# 减
print('3 - 2 =', 3 - 2)  # 3 - 2 = 1
# 乘
print('5 * 8 =', 5 * 8)  # 5 * 8 = 40
# 除
# 得到浮点数，完整的结果
print('5 / 2 =', 5 / 2)  # 5 / 2 = 2.5
# 得到一个整数
print('5 // 2 =', 5 // 2)  # 5 // 2 = 2
# 取余
print('5 % 2 =', 5 % 2)  # 5 % 2 = 1
# 乘方
print('5 ** 2 =', 5 ** 2)  # 5 ** 2 = 25
