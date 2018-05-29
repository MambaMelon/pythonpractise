# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 0:48
# @Author  : melon

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    x = np.arange(-3, 3, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # 创建两个单独的figure
    # plt.figure()
    # plt.plot(x, y1)
    # plt.figure()
    # plt.plot(x, y2)

    # 显示在一个figure中
    # plt.title("测试图像")
    # 指定默认字体
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    # 解决保存图像是负号'-'显示为方块的问题
    mpl.rcParams['axes.unicode_minus'] = False
    # plt.plot(x, y1, x, y2)

    x1 = [1, 2, 3]
    m1 = [5, 7, 4]
    x2 = [5, 7, 4]
    m2 = [1, 2, 3]

    # subplot子图
    plt.subplot(221)
    plt.plot(x1, m1, 'r--')
    plt.subplot(223)
    plt.plot(x2, m2, 'b--')


    plt.show()