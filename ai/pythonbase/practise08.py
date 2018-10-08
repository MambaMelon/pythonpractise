# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 下午 22:45
# @Author  : melon

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    mu = 100
    sigma = 15
    x = np.random.normal(mu, sigma, 10000)

    ax = plt.gca()
    ax.hist(x, bins=500, color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.set_title(r'$\mathrm{Histogram:}\ mu=%d, \ \sigma=%d' % (mu, sigma))

    plt.show()