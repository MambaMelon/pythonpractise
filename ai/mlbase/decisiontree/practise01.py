# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 15:46
# @Author  : melon

import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA #主成分分析
from sklearn.feature_selection import SelectKBest #特征选择
from sklearn.feature_selection import chi2 #卡方统计量
from sklearn.model_selection  import train_test_split#测试集和训练集
from sklearn.preprocessing import MinMaxScaler  #数据归一化
from sklearn.tree import DecisionTreeClassifier #分类树

if __name__ == '__main__':

    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    warnings.filterwarnings('ignore', category=FutureWarning)

    iris_feature_E = 'sepal length', 'sepal width', 'petal length', 'petal width'
    iris_feature_C = '花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度'
    iris_class = 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'

    # 读取数据
    path = '../datasets/iris.data'
    data = pd.read_csv(path, header=None)
    x = data[list(range(4))]
    # 把Y转换成分类型的0,1,2
    y = pd.Categorical(data[4]).codes

    # 示例:将类别转换为数字
    # cate = pd.Categorical(['a', 'c', 'b', 'a', 'd'])
    # cate.codes
    # cate.categories

    x_train1, x_test1, y_train1, y_test1 = train_test_split(x, y, train_size=0.8, random_state=14)
    x_train, x_test, y_train, y_test = x_train1, x_test1, y_train1, y_test1

    # 因为需要体现以下是分类模型，因为DecisionTreeClassifier是分类算法，要求y必须是int类型
    y_train = y_train.astype(np.int)
    y_test = y_test.astype(np.int)

    ss = MinMaxScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)
    print("原始数据各个特征属性的调整最小值:", ss.min_)
    print("原始数据各个特征属性的缩放数据值:", ss.scale_)

    # 在当前的案例中，使用SelectKBest这个方法从4个原始的特征属性，选择出来3个
    # K默认为10.如果指定了，那么就会返回你所想要的特征的个数
    ch2 = SelectKBest(chi2, k=3)
    x_train = ch2.fit_transform(x_train, y_train)  # 训练并转换
    x_test = ch2.transform(x_test)  # 转换

    # 对类别判断影响最大的三个特征属性分布
    select_name_index = ch2.get_support(indices=True)

    # 构建一个pca对象，设置最终维度是2
    pca = PCA(n_components=2)
    x_train = pca.fit_transform(x_train)
    x_test = pca.transform(x_test)

    model = DecisionTreeClassifier(criterion='entropy', max_depth=20, random_state=0)
    model.fit(x_train, y_train)
    y_test_hat = model.predict(x_test)

    # 模型结果的评估
    print(y_test)
    y_test2 = y_test.reshape(-1)
    print(y_test2)
    result = (y_test2 == y_test_hat)
    print("准确率:%.2f%%" % (np.mean(result) * 100))
    print("Score：", model.score(x_test, y_test))
    print("Classes:", model.classes_)
    print("获取各个特征的重要性权重，值越大表示该特征对于目标属性y的影响越大:", end='')
    print(model.feature_importances_)

    # 横纵各采样多少个值
    N = 100
    x1_min = np.min((x_train.T[0].min(), x_test.T[0].min()))
    x1_max = np.max((x_train.T[0].max(), x_test.T[0].max()))
    x2_min = np.min((x_train.T[1].min(), x_test.T[1].min()))
    x2_max = np.max((x_train.T[1].max(), x_test.T[1].max()))

    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, N)
    # 生成网格采样点
    x1, x2 = np.meshgrid(t1, t2)
    # 测试点
    x_show = np.dstack((x1.flat, x2.flat))[0]
    # 预测值
    y_show_hat = model.predict(x_show)
    # 使之与输入的形状相同
    y_show_hat = y_show_hat.reshape(x1.shape)

    # 画图
    plt_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    plt_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])

    plt.figure(facecolor='w')
    ## 画一个区域图
    plt.pcolormesh(x1, x2, y_show_hat, cmap=plt_light)
    # 画测试数据的点信息
    plt.scatter(x_test.T[0], x_test.T[1], c=y_test.ravel(), edgecolors='k', s=150, zorder=10, cmap=plt_dark,
                marker='*')  # 测试数据
    # 画训练数据的点信息
    plt.scatter(x_train.T[0], x_train.T[1], c=y_train.ravel(), edgecolors='k', s=40, cmap=plt_dark)  # 全部数据
    plt.xlabel(u'特征属性1', fontsize=15)
    plt.ylabel(u'特征属性2', fontsize=15)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid(True)
    plt.title(u'鸢尾花数据的决策树分类', fontsize=18)
    # plt.show()

    # 基于原始数据前3列比较一下决策树在不同深度的情况下错误率
    # TODO: 将模型在训练集上的错误率也画在图中
    x_train4, x_test4, y_train4, y_test4 = train_test_split(x.iloc[:, :2], y, train_size=0.7, random_state=14)

    depths = np.arange(1, 15)
    err_list = []
    for d in depths:
        # 仅设置了这二个参数，没有对数据进行特征选择和降维，所以跟前面得到的结果不同
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=d, min_samples_split=10)
        clf.fit(x_train4, y_train4)

        ## 计算的是在训练集上的模型预测能力
        score = clf.score(x_test4, y_test4)
        err = 1 - score
        err_list.append(err)
        print("%d深度，训练集上正确率%.5f" % (d, clf.score(x_train4, y_train4)))
        print("%d深度，测试集上正确率%.5f\n" % (d, score))

    ## 画图
    plt.figure(facecolor='w')
    plt.plot(depths, err_list, 'ro-', lw=3)
    plt.xlabel(u'决策树深度', fontsize=16)
    plt.ylabel(u'错误率', fontsize=16)
    plt.grid(True)
    plt.title(u'决策树层次太多导致的拟合问题(欠拟合和过拟合)', fontsize=18)
    # plt.show()