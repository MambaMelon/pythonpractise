# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 下午 04:47
# @Author  : melon

import re

'''正则表达式使用'''

if __name__ == '__main__':

    content = 'Hello 1234567 World_This is a Regex Demo'

    # 匹配目标
    # result = re.match(r'^Hello\s(\d+)\sWorld.*Demo$', content)
    # 匹配成功返回实例，否则返回none
    # print(result)
    # print(result.span())

    # 贪婪匹配与非贪婪匹配
    # res = re.match('^He.*(\d+).*Demo$', content)
    # print(res.group(1))
    # res01 = re.match('^He.*?(\d+).*Demo$', content)
    # print(res01.group(1))

    # 转义 \
    # 匹配模式 re.S

    # re.search 扫描整个字符串并返回第一个成功的匹配
    # re.findall 以列表形式返回全部能匹配的子串
    # re.sub 替换字符串中每一个匹配的子串后返回替换后的字符串



