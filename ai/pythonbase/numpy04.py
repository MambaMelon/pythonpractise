# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 06:12
# @Author  : melon

import numpy as np

if __name__ == "__main__":

    x = np.arange(4)
    xx = x.reshape(4, 1)
    y = np.ones(5)
    z = np.ones((3, 4))

    # 报错
    # x + y

    # 广播机制进行扩展
    res01 = xx + y

    print()