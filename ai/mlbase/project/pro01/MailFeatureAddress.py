# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 14:27
# @Author  : melon

'''垃圾邮件过滤之特征工程'''

import re

import matplotlib as mpl
import pandas as pd

if __name__ == '__main__':

    # 设置字符集，防止中文乱码
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 1. 文件数据读取
    df = pd.read_csv('../../datasets/result_process01', sep=',', header=None, names=['from', 'to', 'date', 'content', 'label'])

    # 2. 特征工程1 => 提取发件人和收件人的邮件服务器地址
    def extract_email_server_address(str1):
        it = re.findall(r"@([A-Za-z0-9]*\.[A-Za-z0-9\.]+)", str(str1))
        result = ''
        if len(it) > 0:
            result = it[0]
        if not result:
            result = 'unknown'
        return result


    df['to_address'] = pd.Series(map(lambda str: extract_email_server_address(str), df['to']))
    df['from_address'] = pd.Series(map(lambda str: extract_email_server_address(str), df['from']))

    # 2. 特征工程1 => 查看邮件服务器的数量
    print("========to address=======================")
    # print(df['to_address'].value_counts().head(5))
    print(df.to_address.value_counts())
    print("总邮件接收服务器类别数量为:" + str(df.to_address.unique().shape))

    print("========from address=======================")
    # print(df.from_address.value_counts().head(5))
    print("总邮件发送服务器类别数量为:" + str(df.from_address.unique().shape))
    from_address_df = df.from_address.value_counts().to_frame()
    len_less_10_from_address_count = from_address_df[from_address_df.from_address <= 100].shape
    print("发送邮件数量小于10封的服务器数量为:" + str(len_less_10_from_address_count))

    # 查看一下发送邮件最多的五个运营商所发送的所有邮件中的正常邮件和异常邮件的比例情况
    print("所有发送邮件情况")
    print(df.from_address.value_counts().head(5))
    print("所有的正常邮件的发送情况")
    print(df[df.label == 0.0].from_address.value_counts().head(5))
    print("所有的异常邮件的发送情况")
    print(df[df.label == 1.0].from_address.value_counts().head(5))

    # 基于上一个的描述信息，我认为如果发送邮箱是：163.com、126.com、tom.com、12.com的情况下，那么邮件有很大可能属于垃圾邮件
    # 如果发送邮箱是：mail.tsinghua.edu.cn\mails.tsinghua.edu.cn\cernet.com ,那么邮件有很大可能是属于正常邮件的
    # 所以这里根据邮箱的发送运营商，构建一些新的特征属性
    df['from_12'] = pd.Series(map(lambda s: int(s == '12.com'), df['from_address']))
    df['from_163'] = pd.Series(map(lambda s: int(s == '163.com'), df['from_address']))
    df['from_126'] = pd.Series(map(lambda s: int(s == '126.com'), df['from_address']))
    df['from_tom'] = pd.Series(map(lambda s: int(s == 'tom.com'), df['from_address']))
    df['from_unknown'] = pd.Series(map(lambda s: int(s == 'unknown'), df['from_address']))
    df['from_tsinghua'] = pd.Series(
        map(lambda s: int(s == 'mail.tsinghua.edu.cn' or s == 'mail.tsinghua.edu.cn'), df['from_address']))
    df['from_cernet'] = pd.Series(map(lambda s: int(s == 'cernet.com'), df['from_address']))
    print("======================")
    print(int('123'=='123'))

