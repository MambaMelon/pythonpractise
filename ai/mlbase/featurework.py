# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 15:06
# @Author  : melon

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from numpy import vstack, array, nan

iris = load_iris()
X = iris.data
Y = iris.target


"""一、特征预处理"""
# 标准化
# StandardScaler().fit_transform(iris.data)

# 区间缩放
# MinMaxScaler().fit_transform(iris.data)

# 归一化
# Normalizer().fit_transform(iris.data)

# 定量特征二值化
from sklearn.preprocessing import Binarizer
# Binarizer(threshold=3).fit_transform(iris.data)

# 独热编码
from sklearn.preprocessing import OneHotEncoder
# OneHotEncoder().fit_transform(iris.target.reshape(-1, 1))

# 缺失值填充
from sklearn.preprocessing import Imputer
# Imputer().fit_transform(vstack((array([nan, nan, nan, nan]), iris.data)))


# 数据变换
# 多项式变换
from sklearn.preprocessing import PolynomialFeatures
#参数degree为度，默认值为2
# PolynomialFeatures().fit_transform(iris.data)

# 单变元函数转换
from numpy import log1p
from sklearn.preprocessing import FunctionTransformer
# FunctionTransformer(log1p).fit_transform(iris.data)


"""一、特征选择"""
# Filter法
# 方差选择法
from sklearn.feature_selection import VarianceThreshold
# VarianceThreshold(threshold=3).fit_transform(iris.data)

# 相关系数法(计算各个特征对目标值的相关系数以及相关系数的P值)
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr
# SelectKBest(lambda X,Y:np.array(list(map(lambda x:pearsonr(x, Y), X.T))).T[0], k=2).fit_transform(iris.data, iris.target)

# 卡方检验
from sklearn.feature_selection import chi2
# SelectKBest(chi2, k=2).fit_transform(x, y)

# 互信息法
# from minepy import MINE

# Wrapper法
# 递归特征消除法
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
#参数n_features_to_select为选择的特征个数
# RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)

# Embedded法
# 基于惩罚项的特征选择法
from sklearn.feature_selection import SelectFromModel
#带L1惩罚项的逻辑回归作为基模型的特征选择
# SelectFromModel(LogisticRegression(penalty="l1", C=0.1)).fit_transform(iris.data, iris.target)

# 基于树模型的特征选择法
from sklearn.ensemble import GradientBoostingClassifier
# GBDT作为基模型的特征选择
# SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)

"""降维"""
# PCA降维
from sklearn.decomposition import PCA
# 参数n_components为主成分数目
# PCA(n_components=2).fit_transform(iris.data)

# LDA降维
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
# 参数n_components为降维后的维数
# LDA(n_components=2).fit_transform(iris.data, iris.target)

