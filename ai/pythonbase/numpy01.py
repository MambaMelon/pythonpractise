# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 15:11
# @Author  : melon

import numpy as np


if __name__ == "__main__":
    # 通过列表创建
    l1 = [1, 2, 3, 4]

    # 通过元组创建
    l2 = (1, 2, 3, 4)

    # 通过元组列表创建
    l3 = [(1, 2, 3, 4), (5, 6, 7, 8)]

    # 创建多维数组
    l4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr1 = np.array(l4)

    # zeros函数.创建一个元素全为0.的浮点型数组.int设置它的类型
    arr2 = np.zeros((3, 2), int)

    # ones函数.创建一个元素全为1的数组
    arr3 = np.ones((3, 2), int)

    arr4 = np.empty((2, 2))
    print(arr4)