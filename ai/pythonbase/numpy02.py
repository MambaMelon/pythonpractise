# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 23:28
# @Author  : melon

import numpy as np

if __name__ == "__main__":

    arr01 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    arr02 = np.array([[1, 2, 3], [0, 0, 0], [0, 0, 0]])
    # 2.ndim维度.需要用几个数字来表示才能唯一确定这个元素,这个数组就是几维
    ndim = arr01.ndim

    # (3, 3)
    shape = arr01.shape

    # dtype 元素类型

    # itemsize 元素的字节大小

    # size 数组大小

    arr03 = np.array([1, 2])
    arr04 = np.array([2, 2])
    # [1 4]
    a01 = arr03 ** arr04

    arr05 = np.array([[1,2], [2, 1]])
    arr06 = np.array([[2,2], [3, 3]])
    # [[8 8] [7 7]]
    a02 = arr05.dot(arr06)

    arr07 = np.array([[[2, 3, 4, 5],
                       [1, 3, 4, 9]],

                      [[0, 3, 4, 8],
                       [2, 4, 9, 4]],

                      [[1, 4, 5, 8],
                       [2, 5, 6, 8]],

                      [[2, 3, 6, 8],
                       [3, 4, 8, 9]]])
    # [4 9].数组的切片
    a03 = arr07[1][1][1:3]

    # 花式索引
    a04 = arr07[[0, 1, 2], [0, 1, 1]]

    # 通过transpose()或者属性T可以得到转置
    arr08 = np.arange(40).reshape(5, -1)
    a05 = arr08.transpose()
    a06 = arr08.T

    arr09 = np.array([[3, 9], [4, 6]])
    # 横向拉伸2倍
    a07 = np.tile(arr09, 2)
    # 纵向拉伸2倍，横向拉升3倍
    a08 = np.tile(arr09, (2,3))

    print(a08)