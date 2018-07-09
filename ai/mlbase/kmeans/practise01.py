# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 15:51
# @Author  : melon

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

if __name__ == '__main__':

    # 产生模拟数据
    N = 1000
    n_centers = 4
    X, Y = make_blobs(n_samples=N, n_features=2, centers=n_centers, random_state=28)

    # 数据可视化
    plt.scatter(X[:, 0], X[:, 1], c=Y, s=10)
    # plt.show()

    # 模型构建
    model = KMeans(n_clusters=4)
    model.fit(X, Y)

    # 输出模型得到的中心点和目标函数的损失值
    print("中心点坐标:")
    print(model.cluster_centers_)
    print("目标函数的损失值（所有样本到对应簇中心点的距离平方和）：")
    print(model.inertia_)
    print(model.inertia_ / N)

    # 预测
    print(X[:2])
    y_hat = model.predict(X[:10])
    print("预测值:{}".format(y_hat))
    print("实际值:{}".format(Y[:10]))
    print("模型的Score评估值:{}".format(model.score(X, Y)))