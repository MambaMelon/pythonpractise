# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 11:27
# @Author  : melon

'''
电流与功率之间的关系
'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import time
from sklearn.externals import joblib

if __name__ == '__main__':

    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 加载数据
    # 日期、时间、有功功率、无功功率、电压、电流、厨房用电功率、洗衣服用电功率、热水器用电功率
    path1 = '../datasets/household_power_consumption_1000.txt'
    df = pd.read_csv(path1, sep=';', low_memory=False)
    X = df.iloc[:, 2:4]
    Y = df['Global_intensity']

    # 分割数据
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    # 数据归一化
    ss = StandardScaler()
    X_train = ss.fit_transform(X_train)
    X_test = ss.transform(X_test)

    # 训练数据
    lr = LinearRegression()
    lr.fit(X_train, Y_train)

    # 结果预测
    Y_predict = lr.predict(X_test)

    # 预测得分率
    score = lr.score(X_test, Y_test)

    t = np.arange(len(X_test))
    plt.figure(facecolor='w')
    plt.plot(t, Y_test, 'r-', linewidth=2, label='真实值')
    plt.plot(t, Y_predict, 'g-', linewidth=2, label='预测值')
    plt.legend(loc='lower right')
    plt.title("线性回归预测功率与电流之间的关系", fontsize=20)
    plt.grid(b=True)
    plt.show()

    print(score)
