# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 10:56
# @Author  : melon

import pandas as pd


class check_Data(object):
    def read_Data(self, filepath):
        data = pd.read_table(filepath, header=None)
        return data

    def data_explore(self, data):
        print(data.describe())


if __name__ == '__main__':
    cd = check_Data()
    data = cd.read_Data('F:/dd/20181031_weibo/weibo_train_data.txt')
    data.columns = ['用户ID', '微博ID', '发送时间', '转发', '评论', '赞', '内容']
    print(data.head(50))