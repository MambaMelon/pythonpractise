# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 下午 09:27
# @Author  : melon

"""工业蒸汽量预测建模"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

if __name__ == '__main__':

    # (2888, 39)
    df = pd.read_csv(r'F:\dd\20181029_zhengqi\zhengqi_train.txt', sep='\t')
    x_test = pd.read_csv(r'F:\dd\20181029_zhengqi\zhengqi_test.txt', sep='\t')

    # 计算object类型的所有列的对应数据的count值
    # for col in df.select_dtypes(include=['float64']).columns:
    #     print('列{}具有{}个不同的value值'.format(col, len(df[col].unique())))

    X = df.drop(labels=['target'], axis=1)
    Y = df['target']

    # 0.72, 0.70, 0.12
    # lir = LinearRegression()
    # lir.fit(x_train, y_train.astype('int'))
    # y_predict = lir.predict(x_test)
    # mse = np.average((y_predict - y_test) ** 2)

    # 0.97, 0.84, 0.14
    rfr = RandomForestRegressor(n_jobs=-1)
    rfr.fit(X, Y)
    pre = rfr.predict(X)
    y_predict = rfr.predict(x_test)

    mse = np.average((pre - Y) ** 2)

    # 输出结果
    # data = pd.DataFrame(y_predict)
    # data.to_csv(r'F:\dd\20181029_zhengqi\zhengqi_predict.txt', header=False, index=False)


    print(mse)
    print(rfr.score(x_test, y_predict))