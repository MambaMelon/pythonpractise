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
from sklearn.cross_validation import cross_val_score, ShuffleSplit

if __name__ == '__main__':

    # (2888, 39)
    df = pd.read_csv(r'F:\dd\20181029_zhengqi\zhengqi_train.txt', sep='\t')


    # 计算object类型的所有列的对应数据的count值
    # for col in df.select_dtypes(include=['float64']).columns:
    #     print('列{}具有{}个不同的value值'.format(col, len(df[col].unique())))

    X = df.drop(labels=['target'], axis=1)
    Y = df['target']

    rf = RandomForestRegressor(n_jobs=-1)

    scores = []
    for i in range(X.shape[1]):
        score = cross_val_score(rf, X[:, i:i + 1], Y, scoring="r2",
                                cv=ShuffleSplit(len(X), 3, .3))
        scores.append((round(np.mean(score), 3), X[i]))
    print(sorted(scores, reverse=True))

    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9, random_state=28)

    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)

    # 0.72, 0.70, 0.12
    # lir = LinearRegression()
    # lir.fit(x_train, y_train.astype('int'))
    # y_predict = lir.predict(x_test)
    # mse = np.average((y_predict - y_test) ** 2)

    # 0.97, 0.84, 0.14
    rfr = RandomForestRegressor(n_jobs=-1)
    rfr.fit(x_train, y_train)
    y_predict = rfr.predict(x_test)
    mse = np.average((y_predict - y_test) ** 2)

    print(rfr.score(x_train, y_train))
    print(rfr.score(x_test, y_test))
    print(mse)