# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 14:30
# @Author  : melon

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == '__main__':

    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    df = pd.read_csv('./LoanStats.csv', skiprows=1, low_memory=False)

    df.drop('id', 1, inplace=True)
    df.drop('member_id', 'columns', inplace=True)

    # df[u'int_rate'] = df[u'int_rate'].astype(str)
    # df[u'int_rate'] = df[u'int_rate'].apply(lambda x: x.replace('%', ''))
    # df[u'int_rate'] = df[u'int_rate'].astype(float)
    df.int_rate = pd.Series(df.int_rate).str.replace('%', '').astype(float)

    # 删除df中行或者列中所有值为nan的
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # 删除emp_title(参考垃圾邮件过滤中的特征删除)
    # print(df['emp_title'].value_counts())
    df.drop(['emp_title'], 1, inplace=True)

    df.replace('n/a', np.nan, inplace=True)
    df.emp_length.fillna(value=0, inplace=True)
    df['emp_length'].replace(to_replace='[^0-9]+', value='', inplace=True, regex=True)
    df['emp_length'] = df['emp_length'].astype(int)

    # 计算object类型的所有列的对应数据的count值
    for col in df.select_dtypes(include=['object']).columns:
        print('列{}具有{}个不同的value值'.format(col, len(df[col].unique())))

    # 删除一些出现类别数目比较多的object类型的column列数据
    df.drop(['sub_grade', 'issue_d', 'desc', 'title',
             'zip_code', 'addr_state', 'earliest_cr_line',
             'last_pymnt_d', 'next_pymnt_d', 'last_credit_pull_d',
             'settlement_date'], 1, inplace=True)

    df.revol_util = pd.Series(df.revol_util).str.replace('%', '').astype(float)

    # 处理缺省值的情况（处理object数据类型的列）
    ndf = df.select_dtypes(include=['O']).describe().T.assign(missing_pct=df.apply(lambda x: (len(x) - x.count()) / float(len(x))))
    # missing_pct： 删除缺省比较严重的特征
    df.drop(['debt_settlement_flag_date'], 1, inplace=True)
    df.drop(['settlement_status'], 1, inplace=True)

    # 贷后相关的字段删除
    df.drop(['out_prncp', 'out_prncp_inv', 'total_pymnt',
             'total_pymnt_inv', 'total_rec_prncp', 'grade'], 1, inplace=True)
    df.drop(['total_rec_int', 'total_rec_late_fee',
             'recoveries', 'collection_recovery_fee',
             'collection_recovery_fee'], 1, inplace=True)
    df.drop(['last_pymnt_amnt'], 1, inplace=True)
    df.drop(['policy_code'], 1, inplace=True)

    # 处理缺省值的情况
    df.select_dtypes(include=['float']).describe().T. \
        assign(missing_pct=df.apply(lambda x: (len(x) - x.count()) / float(len(x))))
    # 删除缺失率比较高的特征
    df.drop(['settlement_amount', 'settlement_percentage', 'settlement_term', 'mths_since_last_record'], 1, inplace=True)

    # 处理缺省值的情况
    df.select_dtypes(include=['int']).describe().T. \
        assign(missing_pct=df.apply(lambda x: (len(x) - x.count()) / float(len(x))))

    # 替换目标属性的值，1表示好用户，0表示坏用户
    df.loan_status.replace('Fully Paid', int(1), inplace=True)
    df.loan_status.replace('Charged Off', int(0), inplace=True)
    df.loan_status.replace('Does not meet the credit policy. Status:Fully Paid', np.nan, inplace=True)
    df.loan_status.replace('Does not meet the credit policy. Status:Charged Off', np.nan, inplace=True)
    df['loan_status'].value_counts()

    print()