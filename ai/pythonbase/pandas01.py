# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:25
# @Author  : melon

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

if __name__ == "__main__":

    # 一维数组方式创建
    ser01 = Series([1, 3, 5, np.NaN, 9])

    # 字典方式创建
    dict = {'0':1, '1':3, '2':5}
    ser02 = Series(dict)\

    df01 = DataFrame([[1, 2, '语文'], [78, '数学', 3]])

    arr01 = np.array([['Tom', 76], ['Gerry', 98], ['John', 85]])
    # index 行标签; columns 列标签
    df02 = DataFrame(arr01, index=['one', 'two', 'three'], columns=['name', 'score'])

    # pd读取csv文件
    # pd.read_csv("")
    print(df02)