#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/26 22:29
@Author  : cai

examples come from http://www.runoob.com/python/python-exercise-example2.html
"""


# ============== Example 2 ======================================
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
#
# ===============================================================

def pay_award():
    profit = int(input('净利润:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if profit > arr[idx]:
            # 当前区间的利润
            r += (profit - arr[idx]) * rat[idx]
            print('current award=', (profit - arr[idx]) * rat[idx])
            # 重置下一个区间起始奖金数量
            profit = arr[idx]
    return r


if __name__ == '__main__':
    result = pay_award()
    print('award=', result)
