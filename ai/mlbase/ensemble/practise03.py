# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 下午 09:49
# @Author  : melon

"""随机森林用于宫颈癌预测"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import label_binarize
from sklearn import metrics

if __name__ == '__main__':

    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    names = [u'Age', u'Number of sexual partners', u'First sexual intercourse',
             u'Num of pregnancies', u'Smokes', u'Smokes (years)',
             u'Smokes (packs/year)', u'Hormonal Contraceptives',
             u'Hormonal Contraceptives (years)', u'IUD', u'IUD (years)', u'STDs',
             u'STDs (number)', u'STDs:condylomatosis',
             u'STDs:cervical condylomatosis', u'STDs:vaginal condylomatosis',
             u'STDs:vulvo-perineal condylomatosis', u'STDs:syphilis',
             u'STDs:pelvic inflammatory disease', u'STDs:genital herpes',
             u'STDs:molluscum contagiosum', u'STDs:AIDS', u'STDs:HIV',
             u'STDs:Hepatitis B', u'STDs:HPV', u'STDs: Number of diagnosis',
             u'STDs: Time since first diagnosis', u'STDs: Time since last diagnosis',
             u'Dx:Cancer', u'Dx:CIN', u'Dx:HPV', u'Dx', u'Hinselmann', u'Schiller',
             u'Citology', u'Biopsy']
    path = "../datasets/risk_factors_cervical_cancer.csv"
    data = pd.read_csv(path)

    X = data[names[0:-4]]
    Y = data[names[-4:]]

    X = X.replace("?", np.NAN)
    # 对于缺省值，进行数据填充；默认是以列/特征的均值填充
    imputer = Imputer(missing_values="NaN")
    X = imputer.fit_transform(X, Y)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    print("训练样本数量:%d,特征属性数目:%d,目标属性数目:%d" % (x_train.shape[0], x_train.shape[1], y_train.shape[1]))

    # 标准化
    # 分类模型经常使用的是minmaxscaler归一化，回归模型经常用standardscaler
    ss = MinMaxScaler()
    x_train = ss.fit_transform(x_train, y_train)
    x_test = ss.transform(x_test)

    # 降维
    pca = PCA(n_components=2)
    x_train = pca.fit_transform(x_train)
    x_test = pca.transform(x_test)
    x_train.shape

    # 随机森林模型
    # n_estimators：迭代次数，每次迭代为Y产生一个模型
    # max_depth一般不宜设置过大，把每个模型作为一个弱分类器
    forest = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=2, random_state=0)
    forest.fit(x_train, y_train)

    # 模型效果评估
    score = forest.score(x_test, y_test)
    print("准确率:%.2f%%" % (score * 100))

    # 模型预测
    # prodict_proba输出概率
    forest_y_score = forest.predict_proba(x_test)

    print(forest_y_score)

    # 计算ROC值
    forest_fpr1, forest_tpr1, _ = metrics.roc_curve(
        label_binarize(y_test[names[-4]], classes=(0, 1, 2)).T[0:-1].T.ravel(), forest_y_score[0].ravel())
    forest_fpr2, forest_tpr2, _ = metrics.roc_curve(
        label_binarize(y_test[names[-3]], classes=(0, 1, 2)).T[0:-1].T.ravel(), forest_y_score[1].ravel())
    forest_fpr3, forest_tpr3, _ = metrics.roc_curve(
        label_binarize(y_test[names[-2]], classes=(0, 1, 2)).T[0:-1].T.ravel(), forest_y_score[2].ravel())
    forest_fpr4, forest_tpr4, _ = metrics.roc_curve(
        label_binarize(y_test[names[-1]], classes=(0, 1, 2)).T[0:-1].T.ravel(), forest_y_score[3].ravel())
    # AUC值
    auc1 = metrics.auc(forest_fpr1, forest_tpr1)
    auc2 = metrics.auc(forest_fpr2, forest_tpr2)
    auc3 = metrics.auc(forest_fpr3, forest_tpr3)
    auc4 = metrics.auc(forest_fpr4, forest_tpr4)

    print("Hinselmann目标属性AUC值：", auc1)
    print("Schiller目标属性AUC值：", auc2)
    print("Citology目标属性AUC值：", auc3)
    print("Biopsy目标属性AUC值：", auc4)

