# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 09:30
# @Author  : melon

import numpy as np
import pandas as pd

if __name__ == "__main__":

    df = pd.DataFrame({
        'key': ['b', 'b', 'a', 'c', 'a', 'b'],
        'data1': range(6)
    })
    # 离散特征的取值之间没有大小的意义
    # 对离散型特征进行one-hot编码
    dummies = pd.get_dummies(df['key'], prefix='key')

    print(dummies)