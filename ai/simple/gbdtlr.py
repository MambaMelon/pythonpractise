# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 上午 12:19
# @Author  : melon

"""gbdt+lr组合使用"""

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets.samples_generator import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model.logistic import LogisticRegression
from sklearn import metrics

if __name__ == '__main__':

    # X为样本特征, y为样本类别输出
    X, y = make_classification(n_samples=80000)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    X_train, X_train_lr, y_train, y_train_lr = train_test_split(X_train, y_train, test_size=0.5)
    grd = GradientBoostingClassifier(n_estimators=10)
    grd_enc = OneHotEncoder()
    grd_lm = LogisticRegression()
    grd.fit(X_train, y_train)
    grd_enc.fit(grd.apply(X_train)[:, :, 0])
    '''
    使用训练好的GBDT模型构建特征，然后将特征经过one-hot编码作为新的特征输入到LR模型训练。
    '''
    grd_lm.fit(grd_enc.transform(grd.apply(X_train_lr)[:, :, 0]), y_train_lr)
    # 用训练好的LR模型多X_test做预测
    y_pred_grd_lm = grd_lm.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
    # 根据预测结果输出
    fpr_grd_lm, tpr_grd_lm, _ = metrics.roc_curve(y_test, y_pred_grd_lm)

    print(grd.apply(X_train)[:, :, :].shape)


