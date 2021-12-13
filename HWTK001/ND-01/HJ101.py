# -*- coding:utf-8 -*-
"""
HJ101:  输入整型数组和排序标识，对其元素按照升序或降序进行排序

描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序
数据范围： 1<=n<=100，元素大小满足 0<=val<=100000
输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序
输出描述：
输出排好序的数字

示例1
输入：
8
1 2 4 9 3 55 64 25
0
输出：
1 2 3 4 9 25 55 64

示例2
输入：
5
1 2 3 4 5
1
输出：
5 4 3 2 1

"""


def tj_func(array_data, sort_flag):
    if sort_flag not in [0, 1]:
        raise f"第三行输入有误，0代表升序排序，1代表降序排序， 当前输入的是{sort_flag}"
    sort_num_list = reversed(sorted(array_data, reverse=False if int(sort_flag) else True))
    return " ".join(map(str, sort_num_list))


import sys

input_list = []

for index, line in enumerate(sys.stdin):
    remainder = (index + 1) % 3
    input_list.append(line.split())
    if remainder == 0:
        array_count = int(input_list[0][0])
        array_data = [int(x) for x in input_list[1]]
        sort_flag = int(input_list[2][0])
        print(tj_func(array_data, sort_flag))
        input_list = []
