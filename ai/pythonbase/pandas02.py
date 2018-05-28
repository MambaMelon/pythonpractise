# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:55
# @Author  : melon

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

if __name__ == "__main__":

    data = pd.Series([100, 200, 122, 150, 180], index = [['2016', '2016', '2016', '2017', '2017'], ['苹果', '香蕉', '西瓜', '苹果', '西瓜']])

    # 交换索引
    data01 = data.swaplevel().sort_index()

    # 转换为dataframe索引的堆.level表示的是取哪一列为列索引
    data02 = data.unstack(level=1)

    df= DataFrame({
        'year':[2011,2011,2011,2012,2012,2012,2013,2013],
        'fruit':['apple','banana','pear','apple','banana','pear','apple','banana'],
        'production':[1234,1235,1236,1237,1238,1239,1233,1232],
        'profits':[122.12,111.11,132.65,87.98,231.12,322.12,155.12,168.5]
    })
    # 设置分层索引year和fruit.后续统计必须根据这两个索引来
    df01 = df.set_index(['year','fruit'])
    # 根据索引查询值production和profits
    df01.loc[2011, 'apple']
    # 按照fruit的索引分类并求和
    df01.sum(level='fruit')
    # 对列索引进行排序
    df01.set_index(axis=1)
    # 对行索引进行排序
    df01.set_index()
    print(df01)
    print("=======================")
    print()