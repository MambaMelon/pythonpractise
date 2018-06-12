# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 9:26
# @Author  : melon

'''
时间与功率之间的关系
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

    # 日期、时间、有功功率、无功功率、电压、电流、厨房用电功率、洗衣服用电功率、热水器用电功率
    path1 = '../datasets/household_power_consumption_1000.txt'
    df = pd.read_csv(path1, sep=';', low_memory=False)
    # df.info() 查看格式信息
    # df.describe() 查看每列平均数等信息

    # 异常数据处理
    new_df = df.replace('?', np.nan)
    datas = new_df.dropna(axis=0, how='any')

    # 创建一个时间函数格式化字符串
    def date_format(dt):
        t = time.strptime(' '.join(dt), '%d/%m/%Y %H:%M:%S')
        return (t.tm_year, t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)


    # 获取x和y变量, 并将时间转换为数值型连续变量
    X = datas.iloc[:, 0:2]
    X = X.apply(lambda x: pd.Series(date_format(x)), axis=1)
    Y = datas['Global_active_power']

    # X：特征矩阵(类型一般是DataFrame)
    # Y：特征对应的Label标签(类型一般是Series)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    # 数据标准化
    ss = StandardScaler()
    X_train = ss.fit_transform(X_train)
    X_test = ss.transform(X_test)

    # 模型训练
    lr = LinearRegression()
    lr.fit(X_train, Y_train)

    # 模型校验
    y_predict = lr.predict(X_test)
    score_train = lr.score(X_train, Y_train)
    # 预测准确率
    score_test = lr.score(X_test, Y_test)
    mse = np.average((y_predict - Y_test) ** 2)
    rmse = np.sqrt(mse)

    '''
    模型保存/持久化
    在机器学习部署的时候，实际上其中一种方式就是将模型进行输出；另外一种方式就是直接将预测结果输出
    模型输出一般是将模型输出到磁盘文件
    '''
    # 将标准化模型保存
    joblib.dump(ss, "../model/data_ss.model")
    # 将标准化模型保存
    joblib.dump(lr, "../model/data_lr.model")

    # 加载模型
    ss = joblib.load("../model/data_ss.model")
    lr = joblib.load("../model/data_lr.model")

    # 预测
    data1 = [[2006, 12, 17, 12, 25, 0]]
    data1 = ss.transform(data1)
    predict_result = lr.predict(data1)

    t = np.arange(len(X_test))
    plt.figure(facecolor='w')
    plt.plot(t, Y_test, 'r-', linewidth=2, label='真实值')
    plt.plot(t, y_predict, 'g-', linewidth=2, label='预测值')
    plt.legend(loc='upper left')
    plt.title("线性回归预测时间和功率之间的关系", fontsize=20)
    plt.grid(b=True)
    plt.show()

