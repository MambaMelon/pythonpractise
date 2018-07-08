# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 下午 02:47
# @Author  : melon

"""adaboost分类算法"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles

if __name__ == '__main__':

    # 设置属性防止中文乱码
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 构建一个服从高斯正太分布的数据集
    X1, y1 = make_gaussian_quantiles(cov=2.,
                                     n_samples=200, n_features=2,
                                     n_classes=2, random_state=1)
    X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5,
                                     n_samples=300, n_features=2,
                                     n_classes=2, random_state=1)

    X = np.concatenate((X1, X2))
    y = np.concatenate((y1, - y2 + 1))

    # 构建adaboost模型
    # 数据量大的时候，可以增加内部分类器的树深度，也可以不限制树深
    # max_depth树深，数据量大的时候，一般范围在10—100之间
    # 数据量小的时候，一般可以设置树深度较小，或者n_estimators较小
    # n_estimators 迭代次数或者最大弱分类器数：200次
    # base_estimator：DecisionTreeClassifier 选择弱分类器，默认为CART树
    # algorithm：SAMME 和SAMME.R 。运算规则，后者是优化算法，以概率调整权重，迭代速度快，
    # 选择SAMME.R时2，base_estimators需要选择可以计算概率的分类器支持
    # learning_rate：0<v<=1，默认为1，正则项 衰减指数
    # loss：linear、‘square’exponential’。误差计算公式：一般用linear足够
    bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                             algorithm="SAMME.R",  # 可以不写
                             n_estimators=200)
    bdt.fit(X, y)

    plot_step = 0.02
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, plot_step),
                         np.arange(x2_min, x2_max, plot_step))

    # 预测
    Z = bdt.predict(np.c_[xx.ravel(), yy.ravel()])
    # 设置维度
    Z = Z.reshape(xx.shape)

    # 画图
    plot_colors = "br"
    class_names = "AB"

    plt.figure(figsize=(10, 5), facecolor='w')
    # 局部子图
    plt.subplot(121)
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
    for i, n, c in zip(range(2), class_names, plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1],
                    c=c, cmap=plt.cm.Paired,
                    label=u"类别%s" % n)
    # plt.xlim(x1_min, x1_max)
    # plt.ylim(x2_min, x2_max)
    plt.legend(loc='upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(u'AdaBoost分类结果,正确率为:%.2f%%' % (bdt.score(X, y) * 100))

    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, y1, y2 * 1.2))
    plt.legend(loc='upper right')
    plt.ylabel(u'样本数')
    plt.xlabel(u'决策函数值')
    plt.title(u'AdaBoost的决策值')

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.35)
    # plt.show()