# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 9:24
# @Author  : melon

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectFromModel

if __name__ == '__main__':

    # 设置字符集，防止图片中的中文乱码
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 特征之后的数据读取
    data = pd.read_csv("./features01.csv")

    Y = data['loan_status']
    X = data.drop(['loan_status'], 1, inplace=False)
    # print("样本数量为:%d, 特征属性数量为:%d" % X.shape)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    # 一般情况下：在做分类的时候，都会看一下各个类别的样本数量的比例，看一下是否存在数据的不平衡情况
    # print(y_train.value_counts())
    # print(y_test.value_counts())

    # 构造最优参数
    # parameters = {
    #     "penalty": ['l1', 'l2'],
    #     "C": [0.01, 0.1, 1],
    #     "fit_intercept": [True, False],
    #     "max_iter": [100, 150, 200]
    # }
    # clf = GridSearchCV(LogisticRegression(random_state=0), param_grid=parameters, cv=3)
    # clf.fit(x_train, y_train)

    # 得到最优参数
    # print("最优参数:", end="")
    # print(clf.best_params_)

    # 使用逻辑回归来分析数据
    '''
    lr = LogisticRegression(C=0.1, fit_intercept=True, max_iter=100, penalty='l1', random_state=0)
    lr.fit(x_train, y_train)
    train_predict = lr.predict(x_train)
    print("训练集合上的f1指标:%.4f" % f1_score(y_train, train_predict))
    test_predict = lr.predict(x_test)
    print("测试集合上的f1指标:%.4f" % f1_score(y_test, test_predict))
    # 使用逻辑回归来分析数据 + 可以选择给类别添加权重
    # 加入权重后，模型效果变的更差：原因可能是，两个类别之间的比例没有那么悬殊或者数据上来讲两个类别的数据融合在一起的
    weight = {
        0: 5,  # 在模型训练和测试的过程中，类别0的重要性
        1: 1  # 在模型训练和测试的过程中，类别1的重要性
    }
    lr = LogisticRegression(C=0.1,
                            fit_intercept=True,
                            max_iter=100,
                            penalty='l1',
                            random_state=0,
                            class_weight=weight
                            )
    lr.fit(x_train, y_train)
    '''

    # 使用随机森林来分析数据
    '''
    forest = RandomForestClassifier(random_state=0, max_depth=5)
    forest.fit(x_train, y_train)
    train_predict = forest.predict(x_train)
    print("训练集合上的f1指标:%.4f" % f1_score(y_train, train_predict))
    test_predict = forest.predict(x_test)
    print("测试集合上的f1指标:%.4f" % f1_score(y_test, test_predict))
    # 基于随机森林获取影响放贷的二十大因素
    feature_importances = forest.feature_importances_
    feature_importances = 100.0 * (feature_importances / feature_importances.max())
    print(feature_importances)

    indices = np.argsort(feature_importances)[-20:]
    plt.barh(np.arange(20), feature_importances[indices], color='dodgerblue', alpha=0.4)
    plt.yticks(np.arange(20 + 0.25), np.array(X.columns)[indices])
    plt.xlabel('特征重要性百分比')
    plt.title('随机森林20大重要特征提取')
    plt.show()
    '''

    # 用随机森林选择特征，然后使用Logistic回归来做预测
    '''
    print("原始样本大小:{}".format(x_train.shape))
    forest = RandomForestClassifier(random_state=0, max_depth=5)
    # 当特征的权重大于等于给定的threshold的时候，该特征就保留
    # 在决策树类型的算法中，使用SelectFromModel一般选择比0稍大一点点的阈值
    sm = SelectFromModel(estimator=forest, threshold=0.0000001)
    sm.fit(x_train, y_train)
    x_train1 = sm.transform(x_train)
    x_test1 = sm.transform(x_test)
    print("原始样本大小:{}".format(x_train1.shape))
    # b. logistic回归训练
    lr = LogisticRegression(C=0.1, fit_intercept=True, max_iter=100, penalty='l1', random_state=0)
    lr.fit(x_train1, y_train)
    train_predict = lr.predict(x_train1)
    print("训练集合上的f1指标:%.4f" % f1_score(y_train, train_predict))
    test_predict = lr.predict(x_test1)
    print("测试集合上的f1指标:%.4f" % f1_score(y_test, test_predict))
    '''

    # 使用GBDT用于特征选择
    gbdt = GradientBoostingClassifier(min_samples_split=50, max_depth=2, n_estimators=300, learning_rate=0.1,
                                      random_state=0)
    gbdt.fit(x_train, y_train)
    print("权重大于0的特征数目:{}".format(np.sum(gbdt.feature_importances_ > 0)))
    print("权重等于0的特征数目:{}".format(np.sum(gbdt.feature_importances_ == 0)))
    print("权重小于0的特征数目:{}".format(np.sum(gbdt.feature_importances_ < 0)))
    print(gbdt.feature_importances_.shape)
    # x_train = x_train[gbdt.feature_importances_ > 0]
