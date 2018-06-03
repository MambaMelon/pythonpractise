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
    dummies = pd.get_dummies(df['key'], prefix='key')

    print(dummies)