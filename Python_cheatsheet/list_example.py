#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/17 21:47
@Author  : cai

列表知识点
"""

# ===============================================================
# 初始化
# ===============================================================
# 创建空列表，两种方法
list1 = list()
list2 = []
# 初始化带有数据
list3 = [1, 2, 3]
list4 = ['a', 2, 'nb', [1, 3, 4]]

print('list1:', list1)
print('list2:', list2)
print('list3:', list3)
print('list4:', list4)

# ===============================================================
# 增删查找
# ===============================================================
# 末尾添加元素
print('=====增加元素=====')
list1.append("abc")
print('list1.append("abc"), list1:', list1)
# 末尾添加另一个列表，并合并为一个列表
list1.extend(list3)
print('list1.extend(list3), list1:', list1)
list1.extend((1, 3))
print('list1.extend((1,3)), list1:', list1)
# 通过 += 添加元素
list2 += [1, 2, 3]
print('list2 += [1, 2, 3], ist2:', list2)
list2 += list4
print('list2 += list4, list2:', list2)
# 在指定位置添加元素,原始位置元素右移一位
list3.insert(0, "a")
print('list3.insert(0, "a"), list3:', list3)
# 末尾位置添加，原来末尾元素依然保持在末尾
list3.insert(-1, "b")
print('list3.insert(-1, "b"), list3:', list3)
print('=====删除元素=====')
# del 删除指定位置元素
del list3[-1]
print('del list3[-1], list3:', list3)
# pop 删除元素
pop_el = list3.pop()
print('list3:', list3)
print('pop element:', pop_el)
# pop 删除指定位置元素
pop_el2 = list3.pop(0)
print('list3:', list3)
print('pop element:', pop_el2)
# remove 根据值删除元素
list3.remove(1)
print('list3:', list3)
# clear 清空列表
list3.clear()
print('clear list3:', list3)
print('=====查询元素=====')
# index 根据数值查询索引
print('list1:', list1)
ind = list1.index(3)
print('list1.index(3)，index=', ind)
print('=====访问&修改元素=====')
# 访问列表第一个元素
print('list1[0]: ', list1[0])
# 访问列表最后一个元素
print('list1[-1]: ', list1[-1])
# 访问第一个到第三个元素
print('list1[:3]: ', list1[:3])
# 访问第一个到第三个元素,步长为2
print('list1[:3:2]: ', list1[:3:2])
# 复制列表
new_list = list1[:]
print('copy list1, new_list:', new_list)
print('=====排序=====')
list5 = [3, 1, 4, 2, 5]
print('list5:', list5)
# use sorted
list6 = sorted(list5)
print('list6=sorted(list5), list5={}, list6={}'.format(list5, list6))
# use list.sort()
list5.sort()
print('list5.sort(), list5: ', list5)

# 列表元素也是列表
list8 = [[4, 3], [5, 2], [1, 1]]
list9 = sorted(list8)
print('list9 = sorted(list8), list9=', list9)
# sorted by the second element
list10 = sorted(list8, key=lambda x: x[1])
print('list10 = sorted(list8, key=lambda x:x[1]), list10=', list10)
list11 = sorted(list8, key=lambda x: (x[1], x[0]))
print('list11 = sorted(list8, key=lambda x:(x[1],x[0])), list11=', list11)
# 列表元素是字符串
list_str = ['abc', 'pat', 'cda', 'nba']
list_str_1 = sorted(list_str)
print('list_str_1 = sorted(list_str), list_str_1=', list_str_1)
# 根据第二个元素排列
list_str_2 = sorted(list_str, key=lambda x: x[1])
print('list_str_2 = sorted(list_str, key=lambda x: x[1]), list_str_2=', list_str_2)
# 先根据第三个元素，再根据第一个元素排列
list_str_3 = sorted(list_str, key=lambda x: (x[2], x[0]))
print('list_str_3 = sorted(list_str, key=lambda x: (x[2], x[0])), list_str_3=', list_str_3)
print('===反转列表===')
# 反转列表
list5.reverse()
print('list5.reverse(), list5: ', list5)
list7 = reversed(list5)
print('list7=reversed(list5), list5={}, list7={}'.format(list5, list7))
# for val in list7:
#     print(val)
list7_val = [val for val in list7]
print('采用列表推导式, list7_val=', list7_val)
list_reversed = list5[::-1]
print('list5 = {}\nlist_reversed = list5[::-1], list_reversed = {}'.format(list5, list_reversed))

print('===其他===')
# 列表元素求和
list5 = [3, 1, 4, 2, 5]
print('list5:', list5)
sum_list5 = sum(list5)
print('sum_list5=sum(list5), sum_list5=', sum_list5)
# 实现 list_a + list_b 的对应元素相加操作
list_a = [1, 3, 5]
list_b = [2, 4, 6]
sum_pair = [sum(pair) for pair in zip(list_a, list_b)]
print('sum_pair = [sum(pair) for pair in zip(list_a, list_b)], sum_pair =', sum_pair)

# 字符串和列表的相互转换
print('===字符串和列表的相互转换===')
strs = 'python'
list_str = list(strs)
print('strs = {}\nlist_str = list(strs), list_str={}'.format(strs, list_str))
new_strs = '-'.join(list_str)
print('new_strs= ', new_strs)

# 计算某个元素出现的次数
list_c = [2, 3, 2, 2, 1, 4]
count = list_c.count(2)
print('count = list.count(2), count={}'.format(count))
