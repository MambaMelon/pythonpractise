# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 14:25
# @Author  : melon

'''
波士顿房屋租赁价格预测
'''

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
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import metrics

if __name__ == '__main__':

    def notEmpty(s):
        return s != ''

    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

    names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    path = "../datasets/boston_housing.data"
    fd = pd.read_csv(path, header=None)

    data = np.empty((len(fd), 14))

    for i, d in enumerate(fd.values):
        d = map(float, filter(notEmpty, d[0].split(' ')))
        # 根据函数结果是否为真,来过滤list中的项
        data[i] = list(d)

    # 分割数据
    x, y = np.split(data, (13,), axis=1)

    # 转换格式 拉直操作
    y = y.ravel()
    ly = len(y)

    # Pipeline常用于并行调参
    models = [
        Pipeline([
            ('ss', StandardScaler()),
            ('poly', PolynomialFeatures()),
            ('linear', RidgeCV(alphas=np.logspace(-3, 1, 20)))
        ]),
        Pipeline([
            ('ss', StandardScaler()),
            ('poly', PolynomialFeatures()),
            ('linear', LassoCV(alphas=np.logspace(-3,1,20)))
        ]),
    ]

    # 参数字典,字典中的key是属性的名称,value是可选的参数列表
    parameters = {
        "poly__degree": [3,2,1],
        "poly__interaction_only": [True, False],#不产生交互项，如X1*X1
        "poly__include_bias": [True, False],#多项式幂为零的特征作为线性模型中的截距
        "linear__fit_intercept": [True, False]
    }

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Ridge算法:最优参数
    {'linear__fit_intercept': True, 'poly__degree': 2, 'poly__include_bias': False, 'poly__interaction_only': True}
    # Lasso算法:最优参数
    {'linear__fit_intercept': False, 'poly__degree': 3, 'poly__include_bias': True, 'poly__interaction_only': True}

    # Lasso和Ridge模型比较运行图表展示
    titles = ['Ridge', 'Lasso']
    colors = ['g-', 'b-']
    plt.figure(figsize=(16, 8), facecolor='w')
    ln_x_test = range(len(x_test))
    plt.plot(ln_x_test, y_test, 'r-', lw=2, label=u'真实值')

    for t in range(2):
        # 获取模型并设置参数
        # GridSearchCV: 进行交叉验证，选择出最优的参数值出来
        # 第一个输入参数：进行参数选择的模型
        # param_grid： 用于进行模型选择的参数字段，要求是字典类型；cv: 进行几折交叉验证
        model = GridSearchCV(models[t], param_grid=parameters, cv=5, n_jobs=1)  # 五折交叉验证
        # 模型训练-网格搜索
        model.fit(x_train, y_train)
        # 模型效果值获取（最优参数）
        print("%s算法:最优参数:" % titles[t], model.best_params_)
        print("%s算法:R值 = % .3f" % (titles[t], model.best_score_))
        # 模型预测
        y_predict = model.predict(x_test),
        # 画图
        plt.plot(ln_x_test, y_predict, colors[t], lw=t+3, label=u'%s算法估计值,$R^2$=%.3f' % (titles[t], model.best_score_))

    # 图形显示
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.title(u"波士顿房屋价格预测")
    plt.show()

    # 模型训练 ====> 单个Lasso模型（一阶特征选择）<2参数给定1阶情况的最优参数>
    model = Pipeline([
        ('ss', StandardScaler()),
        ('poly', PolynomialFeatures(degree=1, include_bias=True, interaction_only=True)),
        ('linear', LassoCV(alphas=np.logspace(-3, 1, 20), fit_intercept=False))
    ])
    # 模型训练
    model.fit(x_train, y_train)
    print(y.shape[0])
