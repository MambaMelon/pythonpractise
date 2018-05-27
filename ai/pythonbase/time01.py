# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 17:49
# @Author  : melon

import time

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

    print()