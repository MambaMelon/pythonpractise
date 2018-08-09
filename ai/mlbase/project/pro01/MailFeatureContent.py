# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 14:27
# @Author  : melon

'''垃圾邮件过滤之特征工程'''

import re

import matplotlib as mpl
import pandas as pd
import jieba

if __name__ == '__main__':

    # 设置字符集，防止中文乱码
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 1. 文件数据读取
    df = pd.read_csv('../../datasets/result_process01', sep=',', header=None, names=['from', 'to', 'date', 'content', 'label'])

    # 将文本类型全部转换为str类型，然后进行分词操作
    df['content'] = df['content'].astype('str')
    # jieba添加分词字典 jieba.load_userdict("userdict.txt")
    df['jieba_cut_content'] = list(map(lambda st: "  ".join(jieba.cut(st)), df['content']))

    # 特征工程四 ==> 邮件长度对是否是垃圾邮件的影响
    def precess_content_length(lg):
        if lg <= 10:
            return 0
        elif lg <= 100:
            return 1
        elif lg <= 500:
            return 2
        elif lg <= 1000:
            return 3
        elif lg <= 1500:
            return 4
        elif lg <= 2000:
            return 5
        elif lg <= 2500:
            return 6
        elif lg <= 3000:
            return 7
        elif lg <= 4000:
            return 8
        elif lg <= 5000:
            return 9
        elif lg <= 10000:
            return 10
        elif lg <= 20000:
            return 11
        elif lg <= 30000:
            return 12
        elif lg <= 50000:
            return 13
        else:
            return 14

    df['content_length'] = pd.Series(map(lambda st: len(st), df['content']))

    df['content_length_type'] = pd.Series(map(lambda st: precess_content_length(st), df['content_length']))
    df2 = df.groupby(['content_length_type', 'label'])['label'].agg(['count']).reset_index()
    df3 = df2[df2.label == 1][['content_length_type', 'count']].rename(columns={'count': 'c1'})
    df4 = df2[df2.label == 0][['content_length_type', 'count']].rename(columns={'count': 'c2'})
    df5 = pd.merge(df3, df4)
    df5['c1_rage'] = df5.apply(lambda r: r['c1'] / (r['c1'] + r['c2']), axis=1)
    df5['c2_rage'] = df5.apply(lambda r: r['c2'] / (r['c1'] + r['c2']), axis=1)


