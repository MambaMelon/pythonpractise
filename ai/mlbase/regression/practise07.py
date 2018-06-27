# -*- coding: utf-8 -*-
# @Time    : 26 9:34
# @Author  : melon

'''
多项式过拟合
'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV, ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model.coordinate_descent import ConvergenceWarning

if __name__  ==  '__main__':

    # 设置字符集，防止中文乱码
    mpl.rcParams['font.sans-serif']=[u'simHei']
    mpl.rcParams['axes.unicode_minus']=False
    # 拦截异常
    warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

    # 创建模拟数据
    np.random.seed(100)
    # 显示方式设置
    np.set_printoptions(linewidth=1000, suppress=True)
    N = 10
    # 创建等差数列
    x = np.linspace(0, 6, N) + np.random.randn(N)
    y = 1.8 * x ** 3 + x ** 2 - 14 * x - 7 + np.random.randn(N)
    x.shape = -1, 1
    y.shape = -1, 1

    models = [
        Pipeline([
            ('Poly', PolynomialFeatures(include_bias=True)),
            ('Linear', LinearRegression(fit_intercept=False))
        ]),
        Pipeline([
            ('Poly', PolynomialFeatures(include_bias=True)),
            # alpha给定的是Ridge算法中，L2正则项的权重值
            # alphas是给定CV交叉验证过程中，Ridge算法的alpha参数值的取值的范围
            ('Linear', RidgeCV(alphas=np.logspace(-3, 2, 50), fit_intercept = False))
        ]),
        Pipeline([
            ('Poly', PolynomialFeatures(include_bias=True)),
            ('Linear',
                LassoCV(alphas=np.logspace(0, 1, 10), fit_intercept=False))
        ]),
        Pipeline([
            ('Poly', PolynomialFeatures(include_bias=True)),
            # la_ratio：给定EN算法中L1正则项在整个惩罚项中的比例，这里给定的是一个列表；
            # 表示的是在CV交叉验证的过程中，EN算法L1正则项的权重比例的可选值的范围
            ('Linear',
                ElasticNetCV(alphas=np.logspace(0, 1, 10), l1_ratio=[.1, .5, .7, .9, .95, 1], fit_intercept=False))
        ])
    ]

    # 线性模型过拟合图形识别
    plt.figure(facecolor='w')
    degree = np.arange(1, N, 4)
    dm = degree.size
    colors = []
    for c in np.linspace(16711680, 255, dm):
        colors.append('#%06x' % int(c))
    model = models[0]
    for i,d in enumerate(degree):
        plt.subplot(int(np.ceil(dm/2)), 2, i+1)
        plt.plot(x, y, 'ro', ms=10, zorder=N)
        model.set_params(Poly__degree=d)
        model.fit(x, y.ravel())
        lin = model.get_params()['Linear']
        output = u'%d阶，系数为：' % (d)
        # print(output, lin.coef_.ravel())

        x_hat = np.linspace(x.min(), x.max(), num=100)
        x_hat.shape = -1, 1
        y_hat = model.predict(x_hat)
        s = model.score(x, y)
        z = N - 1 if (d == 5) else 0
        label = u'%d阶, 正确率=%.3f' % (d, s)
        plt.plot(x_hat, y_hat, color=colors[i], lw=2, alpha=0.75, label=label, zorder=z)
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.xlabel('X', fontsize=16)
        plt.ylabel('Y', fontsize=16)

    plt.tight_layout(1, rect=(0, 0, 1, 0.95))
    plt.suptitle(u'线性回归过拟合显示', fontsize=22)
    # plt.show()

    print(x)

