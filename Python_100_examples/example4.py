#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/31 17:18
@Author  : cai

examples come from http://www.runoob.com/python/python-exercise-example4.html
"""


# ============== Example 4 ======================================
#  输入某年某月某日，判断这一天是这一年的第几天？
# ===============================================================

def calculate_days():
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    # 统计前 m-1 个月的天数
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    sums = 0
    if 0 < month <= 12:
        sums = months[month - 1]
    else:
        print('Invalid month:', month)

    sums += day

    # 判断闰年
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    if is_leap and month > 2:
        sums += 1
    return sums


if __name__ == '__main__':
    days = calculate_days()
    print('it is the %dth day' % days)
