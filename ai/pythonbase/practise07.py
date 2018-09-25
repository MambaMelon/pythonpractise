# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 下午 09:25
# @Author  : melon

import scipy.misc
from matplotlib.pyplot import *

if __name__ == '__main__':

    x = [1, 2, 3, 4]
    y = [5, 4, 3, 2]

    figure()

    subplot(231)
    plot(x, y)

    subplot(232)
    bar(x, y)

    subplot(233)
    barh(x, y)

    subplot(234)
    bar(x, y)

    y1 = [7, 8, 5, 3]
    bar(x, y1, bottom=y, color='r')

    subplot(235)
    boxplot(x, y)

    subplot(236)
    scatter(x, y)

    show()