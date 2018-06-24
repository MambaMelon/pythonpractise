# -*- coding: utf-8 -*-
# @Time    : 6/11 下午 11:07
# @Author  : melon

'''
最小二乘法
'''

'''
1.直接保存模型对象
2.保存模型预测结果到数据库
'''


from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

if __name__ == '__main__':

    # 设置字符集
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus']=False

    # 日期、时间、有功功率、无功功率、电压、电流、厨房用电功率、洗衣服用电功率、热水器用电功率
    path1 = '../datasets/household_power_consumption_1000.txt'
    df = pd.read_csv(path1, sep=';', low_memory=False)
    X_data = df.iloc[:, 2:4]
    Y_data = df.iloc[:, 5]

    '''
    train_data：所要划分的样本特征集
    train_target：所要划分的样本结果
    test_size：样本占比，如果是整数的话就是样本的数量
    random_state：是随机数的种子
    '''
    X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=0)

    # 将DataFrame转化为矩阵
    X = np.mat(X_train)
    Y = np.mat(Y_train).reshape(-1, 1)

    theta = (X.T * X).I * X.T * Y
    y_hat = np.mat(X_test) * theta

    # 绘制图标
    t = np.arange(len(X_test))
    plt.figure(facecolor='w')
    plt.plot(t, Y_test, 'r-', linewidth=2, label=u'真实值')
    plt.plot(t, y_hat, 'g-', linewidth=2, label=u'预测值')
    plt.legend(loc='lower right')
    plt.title("线性回归预测功率与电流之间的关系", fontsize=20)
    plt.show()