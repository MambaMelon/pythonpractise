# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 13:57
# @Author  : melon

import numpy as np

if __name__ == "__main__":

    arr01 = np.random.randint(1, 9, (2, 2))

    # 平均数,最大值,最小值
    res01 = np.mean(arr01)
    np.amax(arr01)
    np.amin(arr01)

    arr02 = np.array([[1, 2], [2, 4]])
    # 方差
    res02 = np.mean((arr02-arr02.mean())**2)
    # 标准差
    res03 = np.sqrt(np.mean((arr02-arr02.mean())**2))

    # 利用where函数替换特殊值
    arr03 = np.array([[1, 2, np.NaN], [1, 2, 3]])
    condition = np.isnan(arr03)
    res04 = np.where(condition, 0, arr03)

    # 去重函数unique
    print(res04)