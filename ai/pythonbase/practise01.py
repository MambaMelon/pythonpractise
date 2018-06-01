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

    print(res4)