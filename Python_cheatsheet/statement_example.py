#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/17 23:04
@Author  : luocai
@file    : statement_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

条件、循环语句
"""

a = 3
# if 语句
if a > 0:
    print('a =', a)

# if-else
if a > 2:
    print('a is ', a)
else:
    print('a is less 2')

# if-elif-else
if a > 5:
    print('a>5')
elif a > 3:
    print('a>3')
else:
    print('a<=3')

# 嵌套语句
if a < 0:
    print('a<0')
else:
    if a > 3:
        print('a>3')
    else:
        print('0<a<=3')

# while 循环
n = 3
while n > 0:
    print(n)
    n -= 1
# input
promt = "\ninput something, and repeat it."
promt += "\nEnter 'q' to end the program.\n"
message = ""
while message != 'q':
    message = input(promt)
    print(message)


# for
l1 = [i for i in range(3)]
for v in l1:
    print(v)
l2 = ['a', 'b', 'c', 'dd', 'nm']
# 指定区间
for i in range(2, 5):
    print(i)
# 指定区间，并加入步长为 10
for j in range(10, 30, 10):
    print(j)
# 结合 len 来遍历列表
for i in range(len(l2)):
    print('{}: {}'.format(i, l2[i]))
# enumerate()
for i, v in enumerate(l2):
    print('{}: {}'.format(i, v))

# continue
for a in range(5):
    if a == 3:
        continue
    print(a)

# break
for a in range(5):
    if a == 3:
        break
    print(a)

# else
for a in range(5):
    print(a)
else:
    print('finish!')
