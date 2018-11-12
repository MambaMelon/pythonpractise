# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 14:44
# @Author  : melon

import pandas as pd

"""
在真实的业务场景下，我们往往需要对所有商品的一个子集构建个性化推荐模型。
在完成这件任务的过程中，我们不仅需要利用用户在这个商品子集上的行为数据，
往往还需要利用更丰富的用户行为数据。定义如下的符号：
U——用户集合
I——商品全集
P——商品子集，P ⊆ I
D——用户对商品全集的行为数据集合
那么我们的目标是利用D来构造U中用户对P中商品的推荐模型。
"""

if __name__ == '__main__':

    # 最多显示100行
    pd.set_option('display.max_colwidth', 100)
    # 最多显示100列
    pd.set_option('display.max_columns', 100)
    df_user = pd.read_csv(r'F:\dd\20181108_offline\tianchi_fresh_comp_train_user.csv')
    # df_user_sort = df_user.sort_values(by='time', ascending=False)
    df_item = pd.read_csv(r'F:\dd\20181108_offline\tianchi_fresh_comp_train_item.csv')
    print()