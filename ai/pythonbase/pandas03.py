# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:55
# @Author  : melon

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
from dateutil.parser import parse

if __name__ == "__main__":

    # 创建一个时间序列,以3天为一个步长
    date01 = pd.date_range(start='20180520', end='20180530', freq='3D')
    # 创建一个以1s为步长的时间序列
    date02 = pd.date_range(start='20180520 08:21:30', periods=10, freq='s')

    stamp = datetime(2011, 11, 3)
    date04 = str(stamp)
    date03 = stamp.strftime("%Y/%m/%d")
    date05 = parse('2011-1-3')

    long_ts = Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    date06 = long_ts['2000-1']
    # 通过日期进行切片的方式只对规则series有效
    date07 = long_ts[datetime(2000, 12, 1):]
    date08 = long_ts.truncate(before='1/9/2000')
    print(date08)