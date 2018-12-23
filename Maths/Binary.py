#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/22 21:39
@Author  : cai

二进制相关知识，包括转换为十进制，移位操作和逻辑操作
"""


def decimal_to_binary(decimal_val):
    '''
    十进制转为二进制
    :param decimal_val:
    :return:
    '''
    print('transfer %d to binary' % decimal_val)
    recursion_result = change(decimal_val)
    print('递归实现转换结果：', recursion_result)


# 十进制转二进制的方法：除2取余，逆序排列, https://blog.csdn.net/shirley_sweet/article/details/73896279
def change(n):
    result = '0'
    if n == 0:  # 输入为0的情况
        return result
    else:
        result = change(n // 2)  # 调用自身
        return result + str(n % 2)


def binary_to_decimal_func(val):
    '''
    按照定义来实现，即 2^n 的形式
    :param val: str
    :return:
    '''
    print('original val: ', val)
    numbers = len(val)
    result = 0
    for i in range(numbers):
        result += int(val[i]) * pow(2, numbers - i - 1)
    return result


def binary_to_decimal(val):
    '''
    二进制转十进制
    :param val: such as 100101
    :return:
    '''
    # 第一种方法，内建函数--int()，输入值必须是字符串形式
    decimal = int(str(val), 2)
    print('二进制数为: 0b%d' % val)
    print('二进制转换为十进制为：', decimal)
    # 第二种实现方法
    decimal2 = binary_to_decimal_func(str(val))
    print('第二种转换二进制为十进制：', decimal2)


def decimal_to_other_build_function(dec):
    '''
    采用内建函数将十进制转换成二进制、八进制和十六进制
    参考 http://www.runoob.com/python3/python3-conversion-binary-octal-hexadecimal.html
    :param dec:
    :return:
    '''
    print("decimal val：", dec)
    print("binary result：", bin(dec))
    print("octal result：", oct(dec))
    print("hexadecimal result：", hex(dec))


def left_shift(val, n):
    '''
    左移操作
    :param val:
    :param n: 移动的位数
    :return:
    '''

    print('二进制数为: 0b%d' % val)
    val = int(str(val), 2)
    print('十进制数值：', val)
    result = val << n
    print('left shift %d, result=%s' % (n, result))
    result = bin(int(result))
    print('left shift {}, result={}'.format(n, result))


def right_shift(val, n):
    '''
    右移操作
    :param val:
    :param n:
    :return:
    '''
    print('二进制数为: 0b%d' % val)
    val = int(str(val), 2)
    print('十进制数值：', val)
    math_val = val >> n
    print('right shift {}, math_val={}'.format(n, math_val))
    result = bin(int(math_val))
    print('left shift {}, result={}'.format(n, result))


def logic_operation(val1, val2):
    '''
    二进制的逻辑运算，与、或、非以及异或操作
    :param val1:
    :param val2:
    :return:
    '''
    print('orginal val:{},{}'.format(val1, val2))
    dec_val1 = int(str(val1), 2)
    dec_val2 = int(str(val2), 2)
    print('decimal val:{},{}'.format(dec_val1, dec_val2))
    and_result = dec_val1 & dec_val2
    or_result = dec_val1 | dec_val2
    not_result1 = ~dec_val1
    not_result2 = ~dec_val2
    different_or_result = dec_val1 ^ dec_val2
    print('and result：', bin(int(and_result)))
    print('or result：', bin(int(or_result)))
    print('not result1：', bin(int(not_result1)))
    print('not result2：', bin(int(not_result2)))
    print('different or result：', bin(int(different_or_result)))


if __name__ == '__main__':
    dec_val = 53
    binary_val = 100101
    binary_val2 = 110100

    # print('use build function to transform decimal value')
    # decimal_to_other_build_function(dec_val)
    # binary_to_decimal(binary_val)
    # decimal_to_binary(dec_val)
    left_shift(binary_val, 1)
    right_shift(binary_val, 1)
    logic_operation(binary_val, binary_val2)
