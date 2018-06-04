# -*- coding: utf-8 -*-
# @Time    : 6/4 上午 05:42
# @Author  : melon

import json
import numpy as np
import pandas as pd
import os

if __name__ == "__main__":

    f = open(os.getcwd() + '\datasets\\usda_food.json')
    db = json.load(f)
    nutrients = pd.DataFrame(db[0]['nutrients'])

    info_keys = ['description', 'group', 'id', 'manufacturer']
    info = pd.DataFrame(db, columns=info_keys)

    nutrients = []
    for rec in db:
        fnuts = pd.DataFrame(rec['nutrients'])
        fnuts['id'] = rec['id']
        nutrients.append(fnuts)

    nutrients = pd.concat(nutrients, ignore_index=True)
    nutrients.drop_duplicates()

    col_mapping = {'description': 'food', 'group': 'fgroup'}
    info = info.rename(columns=col_mapping, copy=False)

    col_mapping = {'description': 'nutrient', 'group': 'nutgroup'}
    nutrients = nutrients.rename(columns=col_mapping, copy=False)

    ndata = pd.merge(nutrients, info, on='id', how='outer')

    print(nutrients)