# -- encoding:utf-8 --
"""
Create by ibf on 2018/6/30
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.metrics import f1_score, recall_score
import matplotlib as mpl

## 设置属性防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 1. 加载数据
# file_path = 'C:/workspace/python/sklearn07/datas/iris.data'
# file_path = 'file:///C:/workspace/python/sklearn07/datas/iris.data'
file_path = '../datas/iris.data'
names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'cla']
df = pd.read_csv(file_path, header=None, names=names)


# print(df.head())
# print(df.info())


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
# 给定采用gini还是entropy作为纯度的衡量指标
criterion="gini", 
# 进行划分特征选择的时候采用什么方式来选择，best表示每次选择的划分特征都是全局最优的(所有特征属性中的最优划分)；random表示每次选择的划分特征不是所有特征属性中的最优特征，而且先从所有特征中随机的抽取出部分特征属性，然后在这个部分特征属性中选择最优的，也就是random选择的是局部最优。
# best每次都选择最优的划分特征，但是这个最优划分特征其实是在训练集数据上的这一个最优划分。但是这个最优在实际的数据中有可能该属性就不是最优的啦，所以容易陷入过拟合的情况 --> 如果存在过拟合，可以考虑使用random的方式来选择。
splitter="best", 
# 指定构建的决策树允许的最高层次是多少，默认不限制
max_depth=None,
# 指定进行数据划分的时候，当前节点中包含的数据至少要去的数据量
min_samples_split=2,
min_samples_leaf=1,
min_weight_fraction_leaf=0.,
# 在random的划分过程中，给定每次选择局部最优划分特征的时候，使用多少个特征属性
max_features=None,
random_state=None,
max_leaf_nodes=None,
min_impurity_split=1e-7,
class_weight=None,
presort=False
"""
algo = DecisionTreeClassifier(criterion="gini")

# 5. 算法模型的训练
algo.fit(x_train, y_train)

# 6. 模型效果评估
# 看方法的注释的方法：按ctrl键，同时鼠标在方法上左键点击
print("训练集上的准确率:{}".format(algo.score(x_train, y_train)))
print("测试集上的准确率:{}".format(algo.score(x_test, y_test)))
print("训练集上的F1值:{}".format(f1_score(y_train, algo.predict(x_train), average='macro')))
print("测试集上的F1值:{}".format(f1_score(y_test, algo.predict(x_test), average='macro')))
print("训练集上的召回率:{}".format(recall_score(y_train, algo.predict(x_train), average='macro')))
print("测试集上的召回率:{}".format(recall_score(y_test, algo.predict(x_test), average='macro')))

# 7. 模型保存
joblib.dump(algo, './model/algo.m')

# 8. 可视化输出
# 1. 方式一：输出dot文件，然后使用graphviz服务的dot命令将文件转换为pdf或者图像格式
# dot -T pdf iris.dot -o iris.pdf
# dot -T pdf iris.dot -o iris.pdf
from sklearn import tree

with open('./iris.dot', 'w') as f:
    tree.export_graphviz(decision_tree=algo, out_file=f)

# 2. 方式二：直接使用pydotplus插件直接生成pdf文件进行保存
from sklearn import tree
import pydotplus

# feature_names=None, class_names=None 分别给定特征属性和目标属性的name信息
dot_data = tree.export_graphviz(decision_tree=algo, out_file=None,
                                feature_names=['sepal length', 'sepal width', 'petal length', 'petal width'],
                                class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], filled=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("iris2.png")
graph.write_pdf("iris2.pdf")

# 3. 方式三：使用Image对象直接显示pydotplus生成的图片
from sklearn import tree
import pydotplus
from IPython.display import Image

# feature_names=None, class_names=None 分别给定特征属性和目标属性的name信息
dot_data = tree.export_graphviz(decision_tree=algo, out_file=None,
                                feature_names=['sepal length', 'sepal width', 'petal length', 'petal width'],
                                class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], filled=True)
graph = pydotplus.graph_from_dot_data(dot_data)
img = Image(graph.create_png())
print(img)
