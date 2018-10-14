# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 上午 08:11
# @Author  : melon

from urllib import request, error
import socket

if __name__ == '__main__':

    # 异常处理
    try:
        res = request.urlopen('http://www.baidus.com/index.html')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')
    else:
        print('request successfully')