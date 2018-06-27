# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 下午 11:14
# @Author  : melon

''' logistic回归算法应用病理数据分类 '''

import pandas as pd
import numpy as np
import matplotlib as mpl

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':

    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    names = ['id', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
             'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei',
             'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
    path = "../datasets/breast-cancer-wisconsin.data"
    df = pd.read_csv(filepath_or_buffer=path, sep=',', header=None, names=names)
    df = df.replace('?', np.nan)
    df = df.dropna(axis=0, how='any')

    X = df[names[1:10]]
    Y = df[names[10]]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9, random_state=28)

    ss = StandardScaler()
    ss.fit_transform(x_train)

    # penalty: 过拟合解决参数,l1或者l2
    # solver: 参数优化方式
    # 当penalty为l1的时候，参数只能是：liblinear(坐标轴下降法)
    # nlbfgs和cg都是关于目标函数的二阶泰勒展开
    # 当penalty为l2的时候，参数可以是：lbfgs(拟牛顿法)、newton-cg(牛顿法变种)，seg(minibatch)
    # 维度<10000时，lbfgs法比较好，   维度>10000时， cg法比较好，显卡计算的时候，lbfgs和cg都比seg快
    # multi_class: 分类方式参数；参数可选: ovr(默认)、multinomial；
    # 这两种方式在二元分类问题中，效果是一样的；在多元分类问题中，效果不一样
    # ovr: one-vs-rest， 对于多元分类的问题，先将其看做二元分类，分类完成后，再迭代对其中一类继续进行二元分类
    # multinomial: many-vs-many（MVM）,即Softmax分类效果
    # class_weight: 特征权重参数
    algo = LogisticRegression(penalty='l2', fit_intercept=False, C=1.0, max_iter=100, tol=1e-4)
    algo.fit(x_train, y_train)

    print("训练集上模型效果/准确率：{}".format(algo.score(x_train, y_train)))
    print("测试集上模型效果/准确率：{}".format(algo.score(x_test, y_test)))

    # 获取预测值
    print("实际值:")
    print(y_test.ravel())
    y_pred = algo.predict(x_test)
    print("*" * 50)
    print("预测值：(直接返回所属类别)")
    print(y_pred)
    print("*" * 50)
    print("预测值：(返回所属类别的概率)")
    print(algo.predict_proba(x_test))
    print("决策函数值:(也就是线性转换的值θx)")
    print(algo.decision_function(x_test))
    print("预测值：(返回所属类别的概率的log转换值)")
    print(algo.predict_log_proba(x_test))

