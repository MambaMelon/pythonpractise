# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 17:49
# @Author  : melon

import time
from datetime import datetime, timedelta
from dateutil.parser import parse

if __name__ == "__main__":
    # 32400
    # print(time.altzone)

    # Wed Feb 12 13:34:23 2008
    # print(time.asctime((2008, 2, 12, 13, 34, 23, 2, 1, 0)))

    # 时间戳表示的进程时间
    # print(time.clock())

    # time.struct_time(tm_year=2018, tm_mon=5, tm_mday=25, tm_hour=18, tm_min=7, tm_sec=26, tm_wday=4, tm_yday=145, tm_isdst=0)
    # s = time.localtime()

    # 1202794463.0 接收时间元组并返回时间戳
    # s = time.mktime(time.localtime())

    # 格式化日期
    # s = time.strftime("%b %d %Y %H:%M:%S", time.localtime())

    # time.struct_time(tm_year=2008, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=335, tm_isdst=-1)
    # s = time.strptime("30 Nov 08", "%d %b %y")

    # 两个时间之差 1 day, 0:00:01
    delta = datetime(2018, 6, 6) - datetime(2018, 6, 4, 23, 59, 59)

    # 加上一日期
    start = datetime(2018, 6, 5)
    # 2018-06-17 00:00:00
    end1 = start + timedelta(12)
    # 2018-06-29 00:00:00
    end2 = start + 2 * timedelta(12)

    # 字符串与datetime相互转换
    stamp = datetime(2018, 6, 5)
    res01 = str(stamp)
    res02 = stamp.strftime('%Y/%m/%d')
    res03 = datetime.strptime('2018-6-5', '%Y-%m-%d')

    # 2018-06-05 10:59:09
    parse('Tue Jun  5 10:59:09 2018')