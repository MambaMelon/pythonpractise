# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 16:11
# @Author  : melon

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == '__main__':

    # 普通最小二乘法的线性回归
    lr = linear_model.LinearRegression()
    lr.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    # 系数
    lr.coef_

    # alphas参数的交叉验证实现岭回归留一交叉验证
    rcv = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
    rcv.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
    #  rcv.alpha_值越大，缩减量越大，因此系数变得对共线性变得更加鲁棒
    rcv.alpha_

    # lasso回归常用来估计稀疏系数的线性模型
    lasso = linear_model.Lasso(alpha=0.1)
    lasso.fit([[0, 0], [1, 1]], [0, 1])
    lasso.predict([[1, 1]])

    # 贝叶斯回归
    X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
    Y = [0., 1., 2., 3.]
    br = linear_model.BayesianRidge()
    br.fit(X, Y)
    br.predict([[1, 0.]])
    # 模型权重
    br.coef_













