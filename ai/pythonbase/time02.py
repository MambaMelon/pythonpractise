# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 11:03
# @Author  : melon

import time
from datetime import datetime, timedelta
from dateutil.parser import parse
import pandas as pd
import numpy as np

if __name__ == "__main__":

    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
    dup_ts = pd.Series(np.arange(5), index=dates)

    grouped = dup_ts.groupby(level=0)

    # 产生一段时间序列
    res01 = pd.date_range(start='6/5/2018', end='6/15/2018', periods=1)
    # 每月最后一个工作日 BM
    res02 = pd.date_range(start='6/5/2018', end='12/5/2018', freq='BM')
    # 传入指定的时间频率
    res03 = pd.date_range(start='6/5/2018', periods=5, freq='2H30MIN')
    # Week Of Month.每个月第三个礼拜五
    res04 = pd.date_range(start='6/5/2018', end='6/30/2018', freq='WOM-3FRI')


    ts = pd.Series([1, 2, 3, 4], index=pd.date_range('1/1/2000', periods=4, freq='M'))
    # 时间序列向下平移
    res05 = ts.shift(2, freq='M')

    rng = pd.date_range('1/1/2000', periods=5, freq='D')
    ts = pd.Series([1, 2, 3, 2, 1], index=rng)
    # 2000-01    1.8
    res06 = ts.resample('M', kind='period').mean()

    print(ts)
    print(res06)