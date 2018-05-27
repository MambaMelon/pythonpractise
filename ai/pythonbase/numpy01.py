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
    arr01 = np.array(l4)

    # zeros函数.创建一个元素全为0.的浮点型数组.int设置它的类型
    arr02 = np.zeros((3, 2), int)

    # ones函数.创建一个元素全为1的数组
    arr03 = np.ones((3, 2), int)

    arr04 = np.empty((2, 2))

    # [0 2 4 6 8].从0开始到10结束,步长为2
    arr05 = np.arange(0, 10, 2)

    # [ 0.  5. 10.].起始值,最终值以及数组的元素总个数
    arr06 = np.linspace(0, 10, 3)

    # 3行2列不大于1的浮点数数组
    arr07 = np.random.rand(3, 2)

    # 生成2行3列数字在[0,5)之间的数组
    arr08 = np.random.randint(5, size=(2, 3))

    # [0.80570316 0.87428801 0.54497608]
    arr09 = np.random.random_sample(3)

    # [3 4].从一个给定的数组中生成size大小的数组
    arr10 = np.random.choice((1, 2, 3, 4, 5), size=2)
    print(arr10)