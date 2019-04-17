#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/8 22:12
@Author  : luocai
@file    : string_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

"""
s1 = "talk is cheap"
s2 = 'show me the code'
print(s1)
print(s2)

# 索引值以 0 为开始值，-1 为从末尾的开始位置
print('输出 s1 第一个到倒数第二个的所有字符: ', s1[0:-1])  # 输出第一个到倒数第二个的所有字符
print('输出 s1 字符串第一个字符: ', s1[0])  # 输出字符串第一个字符
print('输出 s1 从第三个开始到第六个的字符: ', s1[2:6])  # 输出从第三个开始到第六个的字符
print('输出 s1 从第三个开始后的所有字符:', s1[2:])  # 输出从第三个开始的后的所有字符

# 加号 + 是字符串的连接符
# 星号 * 表示复制当前字符串，紧跟的数字为复制的次数
str = "I love python "
print("连接字符串:", str + "!!!")
print("输出字符串两次:", str * 2)

# 反斜杠 \ 转义特殊字符
# 若不想让反斜杠发生转义，可以在字符串前面添加一个 r
print('I\nlove\npython')
print("反斜杠转义失效:", r'I\nlove\npython')

# strip()
s3 = " I love python "
s4 = "show something!"
print('输出直接调用 strip() 后的字符串结果: ', s3.strip())
print('lstrip() 删除左侧空白后的字符串结果: ', s3.lstrip())
print('rstrip() 删除右侧空白后的字符串结果: ', s3.rstrip())
print('输出调用 strip(\'!\')后的字符串结果: ', s4.strip('!'))
# split()
s5 = 'hello, world'
print('采用split()的字符串结果: ', s5.split())
print('采用split(\',\')的字符串结果: ', s5.split(','))
# join()
l1 = ['an', 'apple', 'in', 'the', 'table']
print('采用join()连接列表 l1 的结果: ', ''.join(l1))
print('采用\'-\'.join()连接列表 l1 的结果: ', '-'.join(l1))
# replace()
print('replace(\'o\', \'l\')的输出结果: ', s5.replace('o', 'l'))
# index()
print('s5.index(\'o\')的输出结果: ', s5.index('o'))
# startswith() / endswith()
print('s5.startswith(\'h\')的输出结果: ', s5.startswith('h'))
print('s5.endswith(\'h\')的输出结果: ', s5.endswith('h'))
# find()
print('s5.find(\'h\')的输出结果: ', s5.find('h'))
# upper() / lower() / title()
print('upper() 字母全大写的输出结果: ', s5.upper())
print('lower() 字母全小写的输出结果: ', s5.lower())
print('title() 单词首字母大写的输出结果: ', s5.title())
