# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 下午 10:57
# @Author  : melon

import scipy.misc
import matplotlib.pyplot as plt

if __name__ == '__main__':

    lena = scipy.misc.ascent()

    plt.gray()
    plt.imshow(lena)
    plt.colorbar()

    print(lena.shape)
    print(lena.max())
    print(lena.dtype)