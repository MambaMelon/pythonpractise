# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 10:19
# @Author  : melon

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import sklearn
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score
from sklearn.ensemble import AdaBoostClassifier,BaggingClassifier

if __name__ == '__main__':

    # 1. 数据的读取
    df = pd.read_csv('./train.csv')

    # X和Y提取
    Y = df['Label']
    X = df.drop(['Label', 'ID', 'V_Time'], 1, inplace=False)

    # 分割
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=24)

    # lr训练
    # lr训练
    # 0.7737&0.7808
    lr = LogisticRegression(penalty='l1', max_iter=1000)

    # 0.8205&0.85
    # lr = LogisticRegression(penalty='l1', max_iter=1000, class_weight={0:1, 1:5}, random_state=28)

    # 0.8585&0.8553
    # lr = DecisionTreeClassifier(class_weight={0: 1, 1: 5}, random_state=28, max_depth=3)

    # 0.9249&0.8590
    # lr1 = DecisionTreeClassifier(class_weight={0:1,1:5}, random_state=28, max_depth=2)
    # lr = AdaBoostClassifier(n_estimators=50, base_estimator=lr1, random_state=28, learning_rate=0.3)

    # 0.8696&0.8645
    # lr1 = DecisionTreeClassifier(class_weight={0:1,1:5}, random_state=28, max_depth=2)
    # lr2 = AdaBoostClassifier(n_estimators=30, base_estimator=lr1, random_state=28, learning_rate=0.3)
    # lr = BaggingClassifier(base_estimator=lr2, n_estimators=100, random_state=28)

    # 0.8460&0.8387
    # lr = SVC(C=0.1, kernel='rbf', gamma=0.001, class_weight={0:1,1:5}, random_state=28)

    # 0.8374&0.8366
    # lr1 = SVC(C=0.1, kernel='rbf', gamma=0.001, class_weight={0:1,1:5}, random_state=28)
    # lr = BaggingClassifier(base_estimator=lr1, n_estimators=10, random_state=28, max_samples=0.7, max_features=0.7)

    lr.fit(x_train, y_train)

    train_predict = lr.predict(x_train)
    print("====训练集上的各个指标====")
    print("F1:%.4f" % f1_score(y_train, train_predict))
    print("召回率:%.4f" % recall_score(y_train, train_predict))
    print("精确率:%.4f" % precision_score(y_train, train_predict))
    print("准确率:%.4f" % accuracy_score(y_train, train_predict))

    test_predict = lr.predict(x_test)
    print("====测试集上的各个指标====")
    print("F1:%.4f" % f1_score(y_test, test_predict))
    print("召回率:%.4f" % recall_score(y_test, test_predict))
    print("精确率:%.4f" % precision_score(y_test, test_predict))
    print("准确率:%.4f" % accuracy_score(y_test, test_predict))