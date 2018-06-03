# -*- coding: utf-8 -*-
# @Time    : 6/4 上午 05:42
# @Author  : melon

import json
import numpy as np
import pandas as pd

if __name__ == "__main__":

    f = open('F:/datasets/pydata-book-2nd-edition/datasets/usda_food/database.json')
    db = json.load(f)
    nutrients = pd.DataFrame(db[0]['nutrients'])

    info_keys = ['description', 'group', 'id', 'manufacturer']
    info = pd.DataFrame(db, columns=info_keys)

    print(db[0:2])