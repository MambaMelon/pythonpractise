# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 15:04
# @Author  : melon

import pandas as pd
import numpy as np
import os

if __name__ == "__main__":

    df = pd.DataFrame({
        'key1': ['a', 'a', 'b', 'b', 'a'],
        'key2': ['one', 'two', 'one', 'two', 'one'],
        'data1': [1, 2, 3, 4, 5],
        'data2': [1, 2, 3, 4, 5]
    })
    grouped = df['data1'].groupby(df['key1'])
    # 按key1分组并求data1的平均值
    grouped.mean()
    # 按key1和key2分组
    means = df['data1'].groupby([df['key1'], df['key2']]).mean()
    means.unstack()

    # 分组键可以是任意长度的数组
    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005, 2005, 2006, 2005, 2006])
    res01 = df['data1'].groupby([states, years]).mean()
    # 返回分组大小
    res02 = df['data1'].groupby([states, years]).size()

    # 对分组进行迭代
    for name, group in df.groupby('key1'):
        name
        group

    # 将数据片段转化为字典
    pieces = dict(list(df.groupby('key1')))

    # 返回Series对象
    df.groupby('key1')['data1']
    # 返回DataFrame对象
    df.groupby('key1')[['data1']]

    # 通过字典或者Series分组
    aa = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
    people = pd.DataFrame(aa, columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
    people.ix[2:3, ['b', 'c']] = np.nan
    mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f': 'orange'}
    by_column = people.groupby(mapping, axis=1)

    map_series = pd.Series(mapping)
    by_series = people.groupby(map_series, axis=1).count()

    # 通过函数进行分组
    by_len = people.groupby(len).sum()

    # 通过aggregate或agg方法传入自己的聚合函数
    def peak_to_peak(arr):
        return arr.max() - arr.min()
    grouped.agg(peak_to_peak)

    path = open(os.getcwd() + '\datasets\\tips.csv')
    tips = pd.read_csv(path)
    tips['tip_pct'] = tips['tip'] / tips['total_bill']
    groupedd = tips.groupby(['smoker', 'time'])
    grouped_pct = groupedd['tip_pct']
    res = grouped_pct.agg('mean')
    # 定义一组应用于全部列的函数
    functions = ['count', 'mean', 'max']
    result = groupedd['total_bill', 'tip_pct'].agg(functions)
    #
    result['tip_pct']

    print()