# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 16:10
# @Author  : melon

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

from sklearn import svm #svm导入
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.exceptions import ChangedBehaviorWarning

if __name__ == '__main__':

    # 设置属性防止中文乱码
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    warnings.filterwarnings('ignore', category=ChangedBehaviorWarning)

    # 读取数据
    # 'sepal length', 'sepal width', 'petal length', 'petal width'
    iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度'
    path = '../datasets/iris.data'
    data = pd.read_csv(path, header=None)
    x, y = data[list(range(4))], data[4]
    # 把文本数据进行编码，比如a b c编码为 0 1 2; 可以通过pd.Categorical(y).categories获取index对应的原始值
    y = pd.Categorical(y).codes
    # 取出第一列和第二列
    # x = x[[0, 1]]
    x =  data.iloc[:, 0:2]

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.8)

    # svm.SVC API说明：
    # 功能：使用SVM分类器进行模型构建
    # 参数说明：
    # C: 误差项的惩罚系数，默认为1.0；一般为大于0的一个数字，C越大表示在训练过程中对于总误差的关注度越高，
    # 也就是说当C越大的时候，对于训练集的表现会越好，但是有可能引发过度拟合的问题(overfiting)
    # kernel：指定SVM内部函数的类型，可选值：linear、poly、rbf、sigmoid、
    # precomputed(基本不用，有前提要求，要求特征属性数目和样本数目一样)；默认是rbf；
    # degree：当使用多项式函数作为svm内部的函数的时候，给定多项式的项数，默认为3
    # gamma：当SVM内部使用poly、rbf、sigmoid的时候，核函数的系数值，当默认值为auto的时候，实际系数为1/n_features
    # coef0: 当核函数为poly或者sigmoid的时候，给定的独立系数，默认为0
    # probability：是否启用概率估计，默认不启动，不太建议启动
    # shrinking：是否开启收缩启发式计算，默认为True
    # tol: 模型构建收敛参数，当模型的的误差变化率小于该值的时候，结束模型构建过程，默认值:1e-3
    # cache_size：在模型构建过程中，缓存数据的最大内存大小，默认为空，单位MB
    # class_weight：给定各个类别的权重，默认为空
    # max_iter：最大迭代次数，默认-1表示不限制
    # decision_function_shape: 决策函数，可选值：ovo和ovr，默认为None；推荐使用ovr；（1.7以上版本才有）

    # gamma值越大，训练集的拟合就越好，但是会造成过拟合，导致测试集拟合变差
    # gamma值越小，模型的泛化能力越好，训练集和测试集的拟合相近，但是会导致训练集出现欠拟合问题，
    # 从而，准确率变低，导致测试集准确率也变低。
    clf = svm.SVC(C=1, kernel='rbf', gamma=0.1)
    clf.fit(x_train, y_train)

    # 计算模型的准确率/精度
    print(clf.score(x_train, y_train))
    print('训练集准确率：', accuracy_score(y_train, clf.predict(x_train)))
    print(clf.score(x_test, y_test))
    print('测试集准确率：', accuracy_score(y_test, clf.predict(x_test)))

    # 计算决策函数的结构值以及预测值(decision_function计算的是样本x到各个分割平面的距离<也就是决策函数的值>)
    print('decision_function:\n', clf.decision_function(x_train))
    print('\npredict:\n', clf.predict(x_train))
