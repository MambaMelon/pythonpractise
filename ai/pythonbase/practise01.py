# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 15:05
# @Author  : melon

import numpy as np
import pandas as pd

if __name__ == "__main__":

    df1 = pd.DataFrame({
        'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
        'date1': range(7)})

    df2 = pd.DataFrame({
        'key': ['a', 'b', 'd'],
        'date2': range(3)})

    # on指定连接.如果key名不同，可以用left_on和right_on指定
    res1 = pd.merge(df1, df2, on='key')

    # how指定连接方式
    res2 = pd.merge(df1, df2, how='right')

    # 如果data数据名称相同,通过suffixes指定后缀区别
    res3 = pd.merge(df1, df2, on='key', suffixes=('_left', '_right'))

    # left_index和right_index表示将索引用于连接键
    res4 = pd.merge(df1, df2, left_index=True, right_index=True)

    # numpy中的轴向连接
    arr = np.arange(12).reshape((3, 4))
    res5 = np.concatenate((arr, arr), axis=1)

    a = pd.Series([np.NaN, 2.5, np.nan, 3.5, 4.5, np.NaN], index=['f', 'e', 'd', 'c', 'b', 'a'])
    b = pd.Series(np.arange(len(a), dtype=np.float64), index=['f', 'e', 'd', 'c', 'b', 'a'])

    # 如果条件成立,则变为b的值,否则变为a的值
    res6 = np.where(pd.isnull(a), b, a)

    df1 = pd.DataFrame({
        'a': [1, np.NaN, 3],
        'b': [np.NaN, 2, 4],
        'c': [5, 6, 7]
    })

    df2 = pd.DataFrame({
        'a': [2, 3, 4, np.NaN],
        'b': [5, 6, 7, 8]
    })

    res7 = df1.combine_first(df2)

    # 统一列的大小写以及增加一列
    data = pd.DataFrame({
        'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami'],
        'ounces': [4, 3, 12, 6]
    })
    meta_to_animal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow'
    }
    data['animal'] = data['food'].map(str.lower).map(meta_to_animal)

    # 离散化和面元划分
    ages = [20, 22, 30, 32, 40]
    bins = [16, 25, 35, 45]
    group_names = ['Youth', 'YouthAdult', 'MiddleAged']
    # [Youth, Youth, YouthAdult, YouthAdult, MiddleAged]
    cats = pd.cut(ages, bins, labels=group_names)
    # [(19.999, 30.0], (19.999, 30.0], (19.999, 30.0], (30.0, 40.0], (30.0, 40.0]]
    res9 = pd.qcut(ages, 2)

    print(res9)