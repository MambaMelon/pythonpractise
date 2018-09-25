# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 9:36
# @Author  : melon

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    X = pd.read_table('vecs_new.txt', header=None, sep=',')
    y = pd.read_table('labels_new.txt', header=None)

    # 将训练集切分为两部分，一部分用于训练GBDT模型
    # 另一部分输入到训练好的GBDT模型生成GBDT特征，然后作为LR的特征
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    X_train, X_train_lr, y_train, y_train_lr = train_test_split(X_train, y_train, test_size=0.5)

    grd = GradientBoostingClassifier(n_estimators=10)
    grd_enc = OneHotEncoder()
    grd_lm = LogisticRegression()

    # 使用X_train训练GBDT模型构造特征
    grd.fit(X_train, y_train)

    y_pred_grd = grd.predict_proba(X_test)[:, 1]
    fpr_grd, tpr_grd, _ = metrics.roc_curve(y_test, y_pred_grd)
    roc_auc = metrics.auc(fpr_grd, tpr_grd)
    print('predict', roc_auc)

    grd_enc.fit(grd.apply(X_train)[:, :, 0])
    grd_lm.fit(grd_enc.transform(grd.apply(X_train_lr)[:, :, 0]), y_train_lr)

    # 用训练好的LR模型多X_test做预测
    y_pred_grd_lm = grd_lm.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
    # 根据预测结果输出
    fpr_grd_lm, tpr_grd_lm, _ = metrics.roc_curve(y_test, y_pred_grd_lm)
    roc_auc = metrics.auc(fpr_grd_lm, tpr_grd_lm)
    print('predict', roc_auc)
    print("AUC Score :", (metrics.roc_auc_score(y_test, y_pred_grd_lm)))
