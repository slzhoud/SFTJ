# -*- coding:utf-8 -*-
"""
HJ15:  求int型正整数在内存中存储时1的个数

描述
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
数据范围：保证在 32 位整型数字范围内
输入描述： 输入一个整数（int类型）
输出描述： 这个数转换成2进制后，输出1的个数

示例1
输入：5
输出：2

示例2
输入：0
输出：0

"""


def tj_func(int_num):
    num_bin = bin(int_num)
    return num_bin.count("1")


import sys

for line in sys.stdin:
    print(tj_func(int(line)))