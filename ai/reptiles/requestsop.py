# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 上午 09:55
# @Author  : melon

import requests
import json


'''requests库操作'''

if __name__ == '__main__':

    # 发起请求
    res01 = requests.get('http://httpbin.org/get')
    # print(res01.status_code)
    # print(res01.cookies)
    # print(res01.text)
    # print(res01.request)
    # 如果返回的是json，直接调用json()
    # print(res01.json())

    # 获取二进制数据
    res02 = requests.get('http://github.com/favicon.ico')
    # print(type(res02.content))
    # print(res02.content)
    # 保存图片
    # with open('favicon.ico', 'wb') as f:
    #     f.write(res02.content)
    #     f.close()

    # 设置请求头
    # headers = {}
    # res03 = requests.get('http://www.baidu.com', headers=headers)

    # 状态码 requests.not_found 或者requests.status_code

    # 文件上传
    # files = {'file': open('favicon.ico', 'rb')}
    # res04 = requests.post('http://httpbin.org/post', files=files)
    # print(res04.text)

    # 获取cookie
    # res = requests.get('http://www.baidu.com')
    # cookies = res.cookies
    # for key, value in cookies.items():
    #     print('key: ' + key + ';value: ' + value)

    # 会话维持
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    res = s.get('http://httpbin.org/cookies')
    print(res.text)

    # 通过get方法还可以设置代理，设置超时，设置认证