# -*- coding: utf-8 -*-
# @Time    : 2016/7/4 15:45
# @Author  : melon

"""RandomTreesEmbedding案例：数据维度扩展"""

import matplotlib as mpl
import pandas as pd
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    # 设置属性防止中文乱码
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 1. 加载数据
    # file_path = 'C:/workspace/python/sklearn07/datas/iris.mnist'
    # file_path = 'file:///C:/workspace/python/sklearn07/datas/iris.mnist'
    file_path = '../datasets/iris.mnist'
    names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'cla']
    df = pd.read_csv(file_path, header=None, names=names)

    # 2. 提取数据
    def parse_record(record):
        result = []
        r = zip(names, record)
        for name, value in r:
            if name == 'cla':
                if value == 'Iris-setosa':
                    result.append(0)
                elif value == 'Iris-versicolor':
                    result.append(1)
                else:
                    result.append(2)
            else:
                result.append(value)
        return result


    datas = df.apply(lambda r: parse_record(r), axis=1)
    # print(datas.head(10))
    # print(datas.cla.value_counts())
    x = datas[names[0:-1]]
    y = datas[names[-1]]

    # 3. 数据的分割
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, random_state=28)

    # 4. 决策树算法模型的构建
    """
    # 随机森林中，子模型决策树的数目。默认为10
    n_estimators=10,
    # 同决策树算法
    criterion="gini",
    # 同决策树算法
    max_depth=None,
    # 同决策树算法
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0.,
    # 同决策树算法
    max_features="auto",
    max_leaf_nodes=None,
    min_impurity_split=1e-7,
    # 给定是否采用有放回的方式产生子数据集，默认为True表示采用。
    bootstrap=True,
    oob_score=False,
    n_jobs=1,
    random_state=None,
    verbose=0,
    warm_start=False,
    class_weight=None
    """
    algo = RandomTreesEmbedding(n_estimators=3, max_depth=3, random_state=28)

    # 5. 算法模型的训练
    algo.fit(x_train, y_train)

    # 6. 直接获取扩展结果
    x_train2 = algo.transform(x_train)
    x_test2 = algo.transform(x_test)
    print("扩展前大小:{}， 扩展后大小:{}".format(x_train.shape, x_train2.shape))
    print("扩展前大小:{}， 扩展后大小:{}".format(x_test.shape, x_test2.shape))


    # 8. 随机森林可视化输出
    print("随机森林中的子模型列表:{}".format(len(algo.estimators_)))
    # 2. 方式二：直接使用pydotplus插件直接生成pdf文件进行保存
    from sklearn import tree
    import pydotplus

    #
    # feature_names=None, class_names=None 分别给定特征属性和目标属性的name信息
    for i in range(len(algo.estimators_)):
        dt = algo.estimators_[i]
        dot_data = tree.export_graphviz(decision_tree=dt, out_file=None,
                                        feature_names=['sepal length', 'sepal width', 'petal length', 'petal width'],
                                        class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], filled=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_png("iris{}.png".format(i))
        graph.write_pdf("iris{}.pdf".format(i))
