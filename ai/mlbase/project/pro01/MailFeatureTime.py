# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 14:27
# @Author  : melon

'''垃圾邮件过滤之特征工程'''
'''没有运行'''

import re

import matplotlib as mpl
import pandas as pd

if __name__ == '__main__':

    df = pd.read_csv('../../datasets/result_process01', sep=',', header=None,
                     names=['from', 'to', 'date', 'content', 'label'])


    def extract_email_date(str1):
        if not isinstance(str1, str):
            str1 = str(str1)

        str_len = len(str1)
        week = ""
        hour = ""
        # 0表示上午[8,12]，1表示下午[13,18],2表示晚上[19,23],3表示凌晨[0,7]
        time_quantum = ""

        if str_len < 10:
            # unknown
            week = "unknown"
            hour = "unknown"
            time_quantum = "unknown"
            pass
        elif str_len == 16:
            # 2005-9-2 上午10:55, 2005-9-2 上午11:04
            rex = r"(\d{2}):\d{2}"
            it = re.findall(rex, str1)
            if len(it) == 1:
                hour = it[0]
            else:
                hour = "unknown"
            week = "Fri"
            time_quantum = "0"
            pass
        elif str_len == 19:
            # Sep 23 2005 1:04 AM
            week = "Sep"
            hour = "01"
            time_quantum = "3"
            pass
        elif str_len == 21:
            # August 24 2005 5:00pm
            week = "Wed"
            hour = "17"
            time_quantum = "1"
            pass
        else:
            rex = r"([A-Za-z]+\d?[A-Za-z]*) .*?(\d{2}):\d{2}:\d{2}.*"
            it = re.findall(rex, str1)
            if len(it) == 1 and len(it[0]) == 2:
                week = it[0][0][-3:]
                hour = it[0][1]
                int_hour = int(hour)
                if int_hour < 8:
                    time_quantum = "3"
                elif int_hour < 13:
                    time_quantum = "0"
                elif int_hour < 19:
                    time_quantum = "1"
                else:
                    time_quantum = "2"
                pass
            else:
                week = "unknown"
                hour = "unknown"
                time_quantum = "unknown"

        week = week.lower()
        hour = hour.lower()
        time_quantum = time_quantum.lower()
        return (week, hour, time_quantum)


    # 数据转换
    date_time_extract_result = list(map(lambda st: extract_email_date(st), df['date']))
    df['date_week'] = pd.Series(map(lambda t: t[0], date_time_extract_result))
    df['date_hour'] = pd.Series(map(lambda t: t[1], date_time_extract_result))
    df['date_time_quantum'] = pd.Series(map(lambda t: t[2], date_time_extract_result))
    df.head(4)

