# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:55
# @Author  : melon

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

if __name__ == "__main__":

    # 创建一个时间序列,以3天为一个步长
    date01 = pd.date_range(start='20180520', end='20180530', freq='3D')
    # 创建一个以1s为步长的时间序列
    date02 = pd.date_range(start='20180520 08:21:30', periods=10, freq='s')
    print(date02)