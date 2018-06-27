# -*- coding: utf-8 -*-
# @Time    : 2016/6/27 9:54
# @Author  : melon

'''葡萄酒质量预测'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import warnings

import sklearn
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV, ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model.coordinate_descent import ConvergenceWarning
from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    ## 设置字符集，防止中文乱码
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    ## 拦截异常
    warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
    warnings.filterwarnings(action='ignore', category=UserWarning)

    path1 = "../datasets/winequality-red.csv"
    df1 = pd.read_csv(path1, sep=";")
    # 设置数据类型为红葡萄酒
    df1['type'] = 1

    path2 = "../datasets/winequality-white.csv"
    df2 = pd.read_csv(path2, sep=";")
    # 设置数据类型为白葡萄酒
    df2['type'] = 0

    # 合并两个df
    df = pd.concat([df1, df2], axis=0)

    # 自变量名称
    names = ["fixed acidity", "volatile acidity", "citric acid",
             "residual sugar", "chlorides", "free sulfur dioxide",
             "total sulfur dioxide", "density", "pH", "sulphates",
             "alcohol", "type"]
    # 因变量名称
    quality = "quality"

    # 异常数据处理
    new_df = df.replace('?', np.nan)
    datas = new_df.dropna(axis=0, how='any')  # 只要有行为空，就进行删除操作

    X = datas[names]
    Y = datas[quality]
    Y.ravel()

    # 创建模型列表
    models = [
        Pipeline([
            ('Poly', PolynomialFeatures()),
            ('Linear', LinearRegression())
        ]),
        Pipeline([
            ('Poly', PolynomialFeatures()),
            ('Linear', RidgeCV(alphas=np.logspace(-4, 2, 20)))
        ]),
        Pipeline([
            ('Poly', PolynomialFeatures()),
            ('Linear', LassoCV(alphas=np.logspace(-4, 2, 20)))
        ]),
        Pipeline([
            ('Poly', PolynomialFeatures()),
            ('Linear', ElasticNetCV(alphas=np.logspace(-4, 2, 20), l1_ratio=np.linspace(0, 1, 5)))
        ])
    ]

    plt.figure(figsize=(16, 8), facecolor='w')
    titles = u'线性回归预测', u'Ridge回归预测', u'Lasso回归预测', u'ElasticNet预测'

    # 将数据分为训练数据和测试数据
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.01, random_state=0)
    ln_x_test = range(len(X_test))

    # 给定阶以及颜色
    # 1 2 3 阶
    d_pool = np.arange(1, 4, 1)
    m = len(d_pool)
    # 颜色
    clrs = []
    for c in np.linspace(5570560, 255, m):
        clrs.append('#%06x' % int(c))

    for t in range(4):
        plt.subplot(2, 2, t + 1)
        model = models[t]
        plt.plot(ln_x_test, Y_test, c='r', lw=2, alpha=0.75, zorder=10, label=u'真实值')
        for i, d in enumerate(d_pool):
            # 设置参数
            model.set_params(Poly__degree=d)
            # 模型训练
            model.fit(X_train, Y_train)
            # 模型预测及计算R^2
            Y_pre = model.predict(X_test)
            # 将Y_pre这种连续性的预测值，转换为离散形式的（转换方式：四舍五入）
            # 既然变成分类的应用的话，那么模型评估指标就不能用R^2，
            # 这里用准确率(两种方式实现，一：numpy原始的实现，二：基于sklearn的相关API实现)
            R = model.score(X_train, Y_train)
            # 输出信息
            lin = model.get_params()['Linear']
            output = u"%s:%d阶, 截距:%d, 系数:" % (titles[t], d, lin.intercept_)
            print(output, lin.coef_)
            # 图形展示
            plt.plot(ln_x_test, Y_pre, c=clrs[i], lw=2, alpha=0.75, zorder=i, label=u'%d阶预测值,$R^2$=%.3f' % (d, R))
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.title(titles[t], fontsize=18)
        plt.xlabel('X', fontsize=16)
        plt.ylabel('Y', fontsize=16)
    plt.suptitle(u'葡萄酒质量预测', fontsize=22)
    plt.show()